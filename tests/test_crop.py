"""Unit fixtures for error handling, not EO release acceptance."""

from datetime import UTC, datetime

import pystac
from click.testing import CliRunner

from cwl_eoap.crop import crop


def test_missing_band_has_clear_error(tmp_path):
    item = pystac.Item("fixture", None, None, datetime(2021, 1, 1, tzinfo=UTC), {})
    path = tmp_path / "item.json"
    item.save_object(dest_href=str(path))
    result = CliRunner().invoke(
        crop,
        ["--input-item", str(path), "--aoi", "0,0,1,1", "--epsg", "EPSG:4326", "--band", "green"],
    )
    assert result.exit_code != 0
    assert isinstance(result.exception, ValueError)
    assert "green" in str(result.exception)


def test_crop_preserves_pixels_and_transform(tmp_path):
    import numpy as np
    import rasterio
    from pystac.extensions.eo import Band, EOExtension
    from rasterio.transform import from_origin

    source = tmp_path / "green.tif"
    pixels = np.arange(256, dtype=np.uint16).reshape(16, 16)
    with rasterio.open(
        source,
        "w",
        driver="GTiff",
        height=16,
        width=16,
        count=1,
        dtype="uint16",
        crs="EPSG:4326",
        transform=from_origin(0, 16, 1, 1),
    ) as raster:
        raster.write(pixels, 1)
    item = pystac.Item("fixture", None, None, datetime(2021, 1, 1, tzinfo=UTC), {})
    item.add_asset("green", pystac.Asset(str(source), roles=["data"]))
    EOExtension.ext(item, add_if_missing=True)
    EOExtension.ext(item.assets["green"]).bands = [Band.create(name="B03", common_name="green")]
    item_path = tmp_path / "item.json"
    item.save_object(dest_href=str(item_path))
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(
            crop,
            [
                "--input-item",
                str(item_path),
                "--aoi",
                "4,4,12,12",
                "--epsg",
                "EPSG:4326",
                "--band",
                "green",
            ],
        )
        assert result.exit_code == 0, result.exception
        with rasterio.open("crop_green.tif") as raster:
            np.testing.assert_array_equal(raster.read(1), pixels[4:12, 4:12])
            assert raster.transform == from_origin(4, 12, 1, 1)
            assert raster.crs.to_epsg() == 4326
