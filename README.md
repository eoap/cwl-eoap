# Application Package and CWL as a solution for Earth Observation portability

The Application Package is a document that describes the data processing application by providing information about the parameters, software item, executable, dependencies and metadata.

The Application Package document ensures that the application is portable among all supporting execution and processing scenarios including the deployment in a Machine-To-Machine (M2M) scenario.

Most importantly, the Application Package information model allows the deployment of the application as an OGC API - Processes (OGC 18-062) compliant web service.

The Application Package includes the following information:

* Reference to the executable block that implements the Application functionality
* Description of its input/output interface

The Application Package uses:

* the Common Workflow Language (CWL) *Workflow* specification as an encoding to describe the Application, its parameters and data flow
* the CWL *CommandLineTool* specification to describe command-line tools, their runtime environments, their arguments and their invocation within containers.

This repository includes the OGC activities that lead to the adoption of the CWL as the open standard for supporting the packaging of Earth Observation applications.

The webpage of the documentation is https://eoap.github.io/cwl-eoap/. 

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
## Typed CWL and PDE validation

Application packages use CWL v1.2, embedded URI records, described ports and
Schema.org repository/version/license/author metadata. Generate and validate
standalone documentation with `python scripts/cwl-docs.py --validate`.
The PDE deployment and executable lab tasks are in the sibling
`dev-platform-eoap/cwl-eoap` folder. Feature-branch changes must be published
or copied into its retained workspace before deployment.

All three notebooks passed on AMD64 Kubernetes on 11 October 2026. The Python
lab asserts successful CLI execution and a raster result; container labs use
the current user's UID/GID, and the package lab exercises typed URI job files.
The rasterio container installs its required native libexpat library.
