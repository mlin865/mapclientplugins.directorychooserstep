Directory Chooser
=================

Overview
--------
The **Directory Chooser** is MAP Client plugin for choosing a directory from a location outside the workflow.


Workflow Connections
--------------------

As shown in :numref:`fig-mcp-directory-chooser-workflow-connections`, the **Directory Chooser** does not need any input.

It produces 1 output which may be piped to other workflow steps:

1. A location where the directory is on the local disk. (Port: *http://physiomeproject.org/workflow/1.0/rdf-schema#directory_location*) 

.. _fig-mcp-directory-chooser-workflow-connections:

.. figure:: _images/workflow-connections.png
   :alt: Directory Chooser workflow connections.
   :align: center
   :figwidth: 75%

   **Directory Chooser** workflow connections.


Information on this plugins' specification is available :ref:`here <mcp-directory-chooser-specification>`.


Configuration
-------------

Information on this plugins' configuration is available :ref:`here <mcp-directory-chooser-configuration>`.


Instructions
------------

This is a non-interactive step.
See `Configuration`_.
