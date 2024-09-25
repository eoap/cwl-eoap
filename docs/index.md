# Application Package and CWL as a solution for Earth Observation portability

The Application Package is a document that describes the data processing application by providing information about the parameters, software item, executable, dependencies and metadata. 

The Application Package document ensures that the application is portable among all supporting execution and processing scenarios including the deployment in a Machine-To-Machine (M2M) scenario. 

Most importantly, the Application Package information model allows the deployment of the application as an OGC API - Processes (OGC 18-062) compliant web service.

The Application Package includes the following information:

*  Reference to the executable block that implements the Application functionality
*  Description of its input/output interface

The Application Package uses:

- the Common Workflow Language (CWL) _Workflow_ specification as an encoding to describe the Application, its parameters and data flow
- the CWL _CommandLineTool_ specification to describe command-line tools, their runtime environments, their arguments and their invocation within containers.

This documentation provides the OGC activities that lead to the adoption of the Common Workflow Language as the open standard for supporting the packaging of Earth Observation applications.