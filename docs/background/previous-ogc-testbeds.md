# Previous OGC testbeds · historical context

This page describes the origins of EOAP. For current adoption and the introductory lesson, start with [EOAP in 20 minutes](../index.md).

The OGC initiatives in Testbed-13, Testbed-14, and Testbed-15 have pioneered the development of an advanced architectural framework designed to facilitate the ad-hoc deployment and execution of applications proximate to the data source. This strategic positioning minimizes data transfer, enhancing efficiency between data repositories and application processes.

These testbeds laid the foundational design for an architecture that supports the encapsulation, deployment, and execution of Earth Observation Applications across distributed Cloud Platforms. This framework ensures that applications are efficiently integrated and managed within cloud environments, providing scalable solutions for Earth Observation data processing.

Building on established OGC standards such as WPS (Web Processing Service) and OWS-Context, these testbed activities have refined the concept of Application Packages. These packages encapsulate data processing applications or workflows, allowing for streamlined deployment and execution across varied Cloud Platforms.

The WPS service plays a pivotal role by enabling end-user portals and B2B client applications to submit processing parameters, initiate on-demand or systematic data processing requests, and establish data pipelines for retrieving the processed information.

Each Application Package contains detailed specifications about the execution units or workflow scripts to be executed, along with configurations for parameterization or customization. This modular approach facilitates the precise tailoring of processing workflows to specific project needs.

The architecture articulated in these testbeds integrates the Application Package with key services: the Execution Management Service (EMS) and the Application Deployment and Execution Service (ADES). The EMS orchestrates the deployment and invocation of processing services workflows, leveraging multiple deployment and execution platforms through WPS-T, a transactional extension of WPS. The ADES, in turn, functions as the execution engine, managing the application lifecycle previously configured as a WPS service by the EMS.

The EMS orchestrates the application package across the selected ADES platform, managing the deployment and execution of workflow components either locally or remotely. It ensures a streamlined operation from deployment to execution, fostering a responsive and agile processing environment.

Primary responsibilities of the ADES include:

- Validating and approving application deployment and execution requests from the EMS.
- Managing the execution of processes within the processing cluster, ensuring robust performance and reliability.
- Monitoring ongoing process execution to maintain operational integrity and performance.
- Retrieving and delivering processed results efficiently, ensuring data integrity and accessibility.

Additionally, the ADES handles critical sub-steps such as the staging-in of input data and the staging-out of output data, essential for maintaining a seamless flow in data processing activities. This comprehensive approach not only enhances operational efficiency but also ensures that the architecture can support complex, data-intensive workflows in an optimized manner.
