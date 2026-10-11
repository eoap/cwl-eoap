# Trace an application package · 8 minutes

Open [quick-start.cwl](https://github.com/eoap/cwl-eoap/blob/main/notebooks/quick-start.cwl) and [inputs.yaml](https://github.com/eoap/cwl-eoap/blob/main/notebooks/inputs.yaml) in the repository's `notebooks/` directory. The snippets below explain selected parts of those files; they are not complete standalone packages.

## 1. Find the public interface · 2 minutes

The CWL document declares `cwlVersion: v1.2`. Its `$graph` contains a `Workflow` with `id: main` and a `CommandLineTool` with `id: rio-bounds`.

The workflow accepts `geotiff` and returns `bounds`. Its input uses a record type named `URI`, imported from the shared EOAP schemas:

```yaml
geotiff:
  type: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#URI
  label: GeoTIFF URI
  doc: URI of the GeoTIFF whose bounding geometry will be returned.
```

The record has one string field, `value`. It comes from the remote `string_format.yaml` schema imported by both the workflow and tool:

```yaml
SchemaDefRequirement:
  types:
    - $import: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml
```

This shared URI convention is also used in the mastering-app-package module; it is not a built-in CWL type or a universal requirement for every EOAP. Resolving the package requires access to the remote schema. Native `File` and `Directory` types have different staging semantics: the runner manages files or directories, whereas this tool reads the URI itself.

## 2. Supply a value · 2 minutes

The job file contains:

```yaml
--8<-- "notebooks/inputs.yaml"
```

The nesting matters: `geotiff` receives a record containing `value`, not a bare URL string. The package also has a default GeoTIFF URI, so a job file can be omitted for the default run.

**Try it on paper:** change `B02.tif` to `B01.tif` in a copy of the job. Which file describes the new execution? The job file; the application package stays the same.

## 3. Follow the command and output · 3 minutes

The workflow connects its input to the tool:

```yaml
steps:
  bounds:
    run: '#rio-bounds'
    in:
      geotiff: geotiff
    out: [bounds]
```

The tool uses `baseCommand: rio` and `arguments: [bounds]`. Its binding extracts the URL:

```yaml
inputBinding:
  position: 1
  valueFrom: $(self.value)
```

Together these construct `rio bounds <GeoTIFF-URL>`. The tool's `stdout: bounds.json` captures the command's output. Its `outputBinding.glob: bounds.json` collects that file, and the workflow's `outputSource: bounds/bounds` exposes it to the caller.

The result is GeoJSON describing the raster's bounding geometry. This example reads raster metadata; it does not produce a cropped raster. The cropping notebooks are a separate, longer exercise.

## 4. Identify the environment · 1 minute

Find `DockerRequirement.dockerPull`, `NetworkAccess` and the `s:` metadata in the complete file. The image supplies `rio`; network access allows the remote GeoTIFF to be read; metadata identifies the application, author, version, license and documentation.

The image `localhost/rio:latest` is built locally for this lesson. A shared deployment needs an image reference the target platform can retrieve, preferably pinned to a digest.

Continue to [build, deploy and run](usage-scenarios.md), then return for the final two-minute check.

## Check your understanding

Answer without running anything:

1. Which class exposes the application's public inputs and outputs?
2. What command runs when `geotiff.value` is supplied?
3. How does `bounds.json` become a workflow result?
4. Can a cloud platform retrieve an image built only on your laptop?

??? success "Check your answers"

    1. The `Workflow` named `main`.
    2. `rio bounds <the supplied URL>` inside the selected container.
    3. `stdout` creates it, the tool collects it with `glob`, and the workflow exposes it through `outputSource`.
    4. The platform needs an accessible registry image or an explicitly supported image-loading mechanism.

You have finished the core lesson when you can explain **input → workflow → container command → output** and name one platform dependency.

## Optional: execute the example after the lesson

Allow extra time for installation, image download and network access. You need `cwltool`, Podman and access to the sample GeoTIFF. In a terminal, start at the repository root:

```sh
cd notebooks
cwltool --validate quick-start.cwl
```

Build the lesson image from a separate Dockerfile; the tracked `notebooks/Dockerfile` is a different GDAL-based example:

```sh
cat > Dockerfile.rio <<'EOF'
FROM docker.io/python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends libexpat1 && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir rasterio==1.5.1 click==8.4.1
ENTRYPOINT []
EOF
podman build -t localhost/rio:latest -f Dockerfile.rio .
cwltool --podman --outdir results quick-start.cwl inputs.yaml
```

A successful run reports the `bounds` output and writes `results/bounds.json`. Inspect that file for GeoJSON geometry. Image failures usually indicate a missing local image; remote-read failures require checking the URL and network access.

For further practice, open [01 Command line](https://github.com/eoap/cwl-eoap/blob/main/notebooks/01%20Command%20line.ipynb), [02 Container](https://github.com/eoap/cwl-eoap/blob/main/notebooks/02%20Container.ipynb), then [03 Package](https://github.com/eoap/cwl-eoap/blob/main/notebooks/03%20Package.ipynb). These are optional labs outside the 20-minute route.
