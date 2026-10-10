cwlVersion: v1.2
class: CommandLineTool
baseCommand: rio
arguments:
- bounds
inputs:
  geotiff:
    type: '#URI'
    default:
      value: https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/10/T/FK/2021/7/S2B_10TFK_20210713_0_L2A/TCI.tif
    inputBinding:
      position: 1
      valueFrom: $(self.value)
    label: geotiff
    doc: geotiff.
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
    - name: '#URI'
      type: record
      fields:
      - name: value
        type: string
$namespaces:
  s: https://schema.org/
s:softwareVersion: 1.0.0
s:codeRepository: https://github.com/eoap/cwl-eoap
s:license: https://spdx.org/licenses/CC-BY-SA-4.0.html
s:author:
- class: s:Person
  s:name: Fabrice Brito
  s:email: fabrice.brito@terradue.com
label: quick-start
doc: 'cwl-eoap: quick-start.'
stdout: bounds.json
