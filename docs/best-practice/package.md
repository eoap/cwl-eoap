# Prepare the package

This is an optional reference after the [20-minute introduction](../index.md). Use the repository's [complete example](https://github.com/eoap/cwl-eoap/blob/main/notebooks/quick-start.cwl) as the starting point, rather than copying incomplete fragments.

## Describe the interface

Use CWL v1.2 for this module. Declare a workflow entrypoint and the tools it invokes. Give processes, steps, inputs and outputs meaningful identifiers, labels and descriptions. Define types deliberately: native `File` and `Directory` inputs support runner-managed staging; the example's imported `URI` record lets its tool read a URL directly.

Connect workflow inputs to step inputs and declare output sources. On each tool, specify the command, argument bindings, container and output collection. Declare required network, expression and resource capabilities where applicable. A workflow may have one step or several; add scatter requirements when a design uses scattering.

## Identify the application

The example uses the `s: https://schema.org/` namespace to record name, description, software version, repository, creation date, license, author, publisher and documentation. Port descriptions explain the interface; application metadata supports discovery and attribution. A validator's metadata profile can impose additional conventions beyond CWL syntax.

## Validate, then execute

From the repository root, in an environment with the dependencies installed:

```sh
cwltool --validate notebooks/quick-start.cwl
python scripts/cwl-docs.py --validate
```

The helper checks this repository's metadata and description conventions, validates with `cwltool`, and renders Markdown under `/tmp/stac-cwl-docs` by default. It is not an EOAP conformance validator. An EOAP validator additionally checks package structure and applicable best-practice rules; check which profiles it reports.

Validation does not prove that an image can be retrieved or an algorithm produces correct results. Run a representative job and inspect its output, then test the target platform's data access and resource requirements.

Practise with [03 Package](https://github.com/eoap/cwl-eoap/blob/main/notebooks/03%20Package.ipynb). The [OGC Best Practice](https://docs.ogc.org/bp/20-089r1.html) is the authoritative reference for requirement wording; the [CWL specifications](https://www.commonwl.org/v1.2/) define execution semantics.
