MAP Client Plugin - Directory Chooser
=====================================

The **Directory Chooser** is MAP Client plugin for choosing a directory from a location outside the workflow.

.. _fig-mcp-directory-chooser-un-configured-step:

.. figure:: _images/un-configured-step.png
   :alt: Un-configured step icon

   An un-configured *Directory Chooser* step icon.

Configure
---------

This step is used for choosing a directory on the local disk from outside the workflow directory.
This step provides a *http://physiomeproject.org/workflow/1.0/rdf-schema#directory_location* to define the location where the directory is on the local disk.
To choose the directory use the *...* button to open a directory chooser dialog.
The *Directory* input is used to hold the relative path from the workflow to the input directory location.

.. _fig-mcp-directory-chooser-configure-dialog:

.. figure:: _images/step-configuration-dialog.png
   :alt: Step configure dialog

   *Directory Chooser* step configuration dialog.

Ports
-----

This plugin:

* **provides**:

  * *http://physiomeproject.org/workflow/1.0/rdf-schema#directory_location*
