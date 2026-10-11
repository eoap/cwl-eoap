# EO Application Packages in 20 minutes

A short introduction to Earth Observation Application Packages (EOAP), using CWL v1.2 and a raster-bounds example. Students learn how job inputs, a workflow, a container command and output files fit together.

Start with the [documentation](https://eoap.github.io/cwl-eoap/) or [lesson source](docs/index.md). The 20-minute route needs no installation: three minutes of context, four minutes on the building blocks, eight minutes tracing the example, three minutes on deployment, and a two-minute knowledge check.

The 2026 perspective includes ESA adoption through the EOEPCA initiative and EOEPCA+, with sources linked in the lesson. Historical OGC testbeds remain available as optional background. The three notebooks are longer, optional practical labs.

## Build the documentation

```sh
python -m pip install mkdocs-material mkdocs-mermaid2-plugin
mkdocs serve
# Check links and configuration:
mkdocs build --strict
```

The site includes the current job-file example directly from `notebooks/inputs.yaml`.

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

## Typed CWL and PDE validation

Application packages use CWL v1.2, shared remote URI schemas, described ports and
Schema.org repository/version/license/author metadata. Generate and validate
standalone documentation with `python scripts/cwl-docs.py --validate`.
The PDE deployment and executable lab tasks are in the sibling
`dev-platform-eoap/cwl-eoap` folder. Feature-branch changes must be published
or copied into its retained workspace before deployment.

All three notebooks passed on AMD64 Kubernetes on 11 October 2026. The Python
lab asserts successful CLI execution and a raster result; container labs use
the current user's UID/GID, and the package lab exercises typed URI job files.
The rasterio container installs its required native libexpat library.
