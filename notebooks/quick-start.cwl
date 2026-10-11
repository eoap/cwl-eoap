cwlVersion: v1.2
$namespaces:
  s: https://schema.org/
s:softwareVersion: 1.0.0
s:codeRepository: https://github.com/eoap/cwl-eoap
s:license: https://spdx.org/licenses/CC-BY-SA-4.0.html
s:author:
- class: s:Person
  s:name: Fabrice Brito
  s:email: fabrice.brito@terradue.com
  s:givenName: Fabrice
  s:familyName: Brito
  s:affiliation:
    class: s:Organization
    s:name: Terradue
s:name: Raster bounds quick start
s:description: Read a remote GeoTIFF and return its bounding geometry as GeoJSON using
  rasterio.
s:dateCreated: '2024-04-04'
s:softwareHelp:
  class: s:CreativeWork
  s:name: CWL for Earth Observation documentation
  s:url: https://eoap.github.io/cwl-eoap/
s:publisher:
  class: s:Organization
  s:name: Terradue
$graph:
- class: Workflow
  id: main
  label: Raster bounds quick start
  doc: Read a remote GeoTIFF and return its bounding geometry as GeoJSON using rasterio.
  requirements:
    SchemaDefRequirement:
      types:
      - $import: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml
  inputs:
    geotiff:
      type: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#URI
      default:
        value: https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/10/T/FK/2021/7/S2B_10TFK_20210713_0_L2A/TCI.tif
      label: GeoTIFF URI
      doc: URI of the GeoTIFF whose bounding geometry will be returned.
  outputs:
    bounds:
      type: File
      label: Raster bounds
      doc: GeoJSON raster bounds.
      outputSource: bounds/bounds
  steps:
    bounds:
      run: '#rio-bounds'
      in:
        geotiff: geotiff
      out:
      - bounds
      label: Read raster bounds
      doc: Retrieve the GeoTIFF bounding geometry with rio bounds.
- class: CommandLineTool
  baseCommand: rio
  arguments:
  - bounds
  inputs:
    geotiff:
      type: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#URI
      default:
        value: https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/10/T/FK/2021/7/S2B_10TFK_20210713_0_L2A/TCI.tif
      inputBinding:
        position: 1
        valueFrom: $(self.value)
      label: GeoTIFF URI
      doc: URI of the GeoTIFF whose bounding geometry will be returned.
  outputs:
    bounds:
      type: File
      label: Raster bounds
      doc: GeoJSON raster bounds.
      outputBinding:
        glob: bounds.json
  requirements:
    DockerRequirement:
      dockerPull: localhost/rio:latest
    NetworkAccess:
      networkAccess: true
    InlineJavascriptRequirement: {}
    SchemaDefRequirement:
      types:
      - $import: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml
  label: Read raster bounds
  doc: Run rasterio rio bounds on a remotely accessible GeoTIFF and capture its GeoJSON
    output.
  stdout: bounds.json
  id: rio-bounds
