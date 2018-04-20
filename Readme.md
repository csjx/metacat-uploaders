# Metacat Uploaders

This module provides classes to upload contents to a Metacat repository via means that are not direct API calls for the content.  It is useful when there are large volumes to register into the server, and where you want to avoid the HTTPS overhead of the web APIs. It currently focuses on an SFTP uploader.