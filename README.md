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

The notebook environment targets Python 3.12. `requirements-notebooks.in`
records the PDE's direct dependencies; `requirements-notebooks.txt` locks all
resolved packages and their hashes. Podman remains a system dependency.

Install the environment and register both notebook kernels:

```sh
uv venv --python 3.12 .venv
uv pip sync --python .venv/bin/python --require-hashes requirements-notebooks.txt
.venv/bin/python -m ipykernel install --user --name cwl_env --display-name "Python (cwl-eoap)"
.venv/bin/python -m bash_kernel.install
source .venv/bin/activate
```

Refresh the lock deliberately, then execute all three notebooks before accepting
the new versions:

```sh
uv pip compile requirements-notebooks.in --python-version 3.12 --generate-hashes --upgrade --output-file requirements-notebooks.txt
```

The sibling PDE's `cwl-eoap/files/init.sh` uses Python 3.12 and installs this
lock with `uv pip sync --require-hashes`, retaining its kernel registration and
PATH setup. Publish the lock with the training source or copy it into the PDE
workspace before deploying the updated initialization script.

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

## Release acceptance

The `Notebook acceptance` workflow installs the hash-locked Python 3.12
notebook environment and Podman, validates the standalone CWL and generated
Markdown, executes all three notebooks with real EO inputs, and builds the
site strictly. Executed notebooks and documentation are retained as CI artifacts.
Run the same notebooks locally with:

```sh
source .venv/bin/activate
python scripts/run-notebooks.py --workspace "$PWD" --notebooks-dir notebooks --python-kernel cwl_env --output /tmp/cwl-eoap-acceptance
```

Notebook cells deliberately generate files and build local teaching containers.
Start acceptance from a clean checkout of the intended release commit. Release
promotion requires successful acceptance of that commit; the CWL currently
identifies the module version as `1.0.0`.
