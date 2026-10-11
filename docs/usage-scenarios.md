# Build, deploy and run · 3 minutes

The same package can support local testing and platform execution. The surrounding services depend on the platform.

| Phase | Application developer or user | Runner or platform |
| --- | --- | --- |
| Build | Write a CLI, build its image, describe the interface in CWL, validate and test | Execute a test job with a CWL runner |
| Deploy | Publish accessible artifacts and request onboarding | Check package support, permissions, image policy and resources |
| Run | Supply input values and request execution | Resolve data access, schedule tools, monitor the job and return outputs |

## Local execution

A CWL runner such as `cwltool` reads the package and job values, starts the container and collects declared outputs. In this lesson the tool reads a remote GeoTIFF directly. Other applications may require input downloads or output uploads, often called **stage-in** and **stage-out**.

## Platform execution in 2026

OGC API — Processes can expose a packaged application as a service: clients discover its interface, submit jobs and retrieve results. Deployment requires the platform's supported onboarding mechanism; an execution API alone does not imply arbitrary package deployment. The [OGC EOAP Best Practice](https://docs.ogc.org/bp/20-089r1.html) describes the package-to-process mapping.

ESA's EOEPCA initiative supplies reusable platform building blocks for this lifecycle. Its Processing architecture describes deployment of OGC Application Packages and execution of their CWL workflows, with a runner handling computation on Kubernetes. This connects the package you write to a platform service that schedules work and manages results. [EOEPCA processing architecture](https://eoepca.readthedocs.io/projects/architecture/en/latest/reference-architecture/processing-BB/).

## What remains platform-specific?

The package describes computation. The deployment supplies identity, credentials, storage, scheduling and quotas. For a remote deployment, check that the image is accessible, data references can be resolved, required CWL features are supported and resource requests fit the platform.

**Discuss:** your package runs locally but fails on another platform. If its image exists only as `localhost/rio:latest`, what needs to change? Publish the image to an accessible registry and update the package reference before investigating the processing logic.

Finish with the [two-minute knowledge check](quick-start.md#check-your-understanding).
