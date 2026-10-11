# The building blocks · 4 minutes

The **Common Workflow Language (CWL)** describes tools and workflows in a form that a runner can interpret. It separates an application's interface from the machine that executes it. This module uses CWL v1.2; consult the [CWL specifications](https://www.commonwl.org/v1.2/) for the complete language.

## Four things to recognise

| Building block | Responsibility | In our example |
| --- | --- | --- |
| Container image | Supplies executable software and libraries | Rasterio and its `rio` command |
| `CommandLineTool` | Maps typed inputs to a command and collects files | `rio bounds <URL>` → `bounds.json` |
| `Workflow` | Exposes the application interface and connects steps | `main` runs the `rio-bounds` tool |
| Job file | Supplies values for one execution | `geotiff.value` contains a GeoTIFF URL |

A workflow can have one step. It provides a stable public interface even when the implementation later grows to several steps.

## Read the execution contract

`inputs` and `outputs` declare names and types. `inputBinding` tells the runner how to construct arguments. `outputBinding.glob` tells it which files to collect. A tool runs in its own working directory; write results there so the runner can retrieve them.

`requirements` state capabilities needed to execute the tool. In our example, `DockerRequirement` selects the image, `NetworkAccess` permits remote data access, and `SchemaDefRequirement` imports the shared URI schema. `InlineJavascriptRequirement` permits the expression that extracts the URL from that record. A requirement must be supported; a `hint` is optional advice to a runner.

## What travels with the package?

The CWL document contains the interface, workflow, software references and metadata. Container images are separate artifacts referenced by the document. Job values are separate too, so you can process different data without rewriting the package.

Portability depends on a compatible runner, accessible images, data permissions and sufficient resources. A container helps reproduce the software environment; recording image digests, input versions and parameters helps reproduce a result.

Continue to [trace the raster-bounds example](../quick-start.md). If YAML is unfamiliar, take the [one-minute syntax reference](../yaml.md) alongside it.
