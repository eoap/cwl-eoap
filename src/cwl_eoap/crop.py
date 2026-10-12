import os

import click
import pystac
import rasterio
from loguru import logger
from pyproj import Transformer
from pystac.extensions.eo import EOExtension
from rasterio.mask import mask
from shapely import box


def aoi2box(aoi: str) -> list[float]:
    """Converts an area of interest expressed as a bounding box to a list of floats"""
    return [float(c) for c in aoi.split(",")]


def get_asset(item: pystac.Item, common_name: str) -> pystac.Asset:
    """Returns the asset of a STAC Item defined with its common band name"""
    for asset in item.assets.values():
        if "data" not in (asset.roles or []):
            continue
        if any(band.common_name == common_name for band in EOExtension.ext(asset).bands or []):
            return asset
    raise ValueError(f"Common band name {common_name} not found in the assets")


def read_item(href: str) -> pystac.Item:
    source = os.path.join(href, "catalog.json") if os.path.isdir(href) else href
    document = pystac.read_file(source)
    if isinstance(document, pystac.Item):
        return document
    if isinstance(document, pystac.Catalog):
        item = next(document.get_all_items(), None)
        if item is not None:
            return item
    raise ValueError("Input must contain a STAC Item")


@click.command(
    short_help="Crop",
    help="Crops a STAC Item asset defined with its common band name",
)
@click.option(
    "--input-item",
    "item_url",
    help="STAC Item URL or staged STAC catalog",
    required=True,
)
@click.option(
    "--aoi",
    "aoi",
    help="Area of interest expressed as a bounding box",
    required=True,
)
@click.option(
    "--epsg",
    "epsg",
    help="EPSG code",
    required=True,
)
@click.option(
    "--band",
    "band",
    help="Common band name",
    required=True,
)
def crop(item_url: str, aoi: str, band: str, epsg: str) -> None:

    item = read_item(item_url)

    logger.info(f"Read {item.id} from {item.get_self_href()}")

    asset = get_asset(item, band)
    logger.info(f"Read asset {band} from {asset.get_absolute_href()}")

    bbox = aoi2box(aoi)

    with rasterio.open(asset.get_absolute_href()) as src:
        transformer = Transformer.from_crs(epsg, src.crs, always_xy=True)

        minx, miny = transformer.transform(bbox[0], bbox[1])
        maxx, maxy = transformer.transform(bbox[2], bbox[3])

        transformed_bbox = box(minx, miny, maxx, maxy)

        logger.info(f"Crop {asset.get_absolute_href()}")

        out_image, out_transform = mask(src, [transformed_bbox], crop=True)
        out_meta = src.meta.copy()

        out_meta.update(
            {
                "height": out_image.shape[1],
                "width": out_image.shape[2],
                "transform": out_transform,
                "dtype": "uint16",
                "driver": "COG",
                "tiled": True,
                "compress": "lzw",
                "blockxsize": 256,
                "blockysize": 256,
            }
        )

        with rasterio.open(f"crop_{band}.tif", "w", **out_meta) as dst_dataset:
            logger.info(f"Write crop_{band}.tif")
            dst_dataset.write(out_image)

    logger.info("Done!")


if __name__ == "__main__":
    crop()
