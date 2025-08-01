
"""
MAP Client Plugin
"""

__version__ = '0.2.2'
__author__ = 'Hugh Sorby'
__stepname__ = 'Directory Chooser'
__location__ = 'https://github.com/mapclient-plugins/mapclientplugins.directorychooserstep'

# import class that derives itself from the step mountpoint.
from mapclientplugins.directorychooserstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
