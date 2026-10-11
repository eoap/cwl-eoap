# How CWL fits EOAP

The [OGC Best Practice for Earth Observation Application Package](https://docs.ogc.org/bp/20-089r1.html) uses CWL to describe an application interface, its workflow and the containerised tools it invokes.

The `Workflow` supplies the public application interface. `CommandLineTool` descriptions supply commands, argument bindings and container requirements. A platform can use that interface to describe a remotely callable process, while a local CWL runner can execute the same computation with a job file.

CWL is a general workflow language used beyond Earth Observation. EOAP adds EO packaging guidance, metadata and data handling patterns. STAC can describe input and output data assets in those patterns; the lesson's small raster-bounds example simply accepts a GeoTIFF URI and returns a file.

Start with [the building blocks](nutshell.md) and [the guided example](../quick-start.md). For wider workflows, explore the community's [application package patterns](https://eoap.github.io/application-package-patterns/).
