# Standard library
import os

# Pyblish libraries
import pyblish
import pyblish.api

# Local libraries
from pyblish_photoshop import plugins


def register_host():
    """Register supported hosts"""
    pyblish.api.register_host("photoshop")


def deregister_host():
    """Register supported hosts"""
    pyblish.api.deregister_host("photoshop")


def register_plugins():
    # Register accompanying plugins
    plugin_path = os.path.dirname(plugins.__file__)
    pyblish.api.register_plugin_path(plugin_path)
    print("pyblish: Registered %s" % plugin_path)


def deregister_plugins():
    plugin_path = os.path.dirname(plugins.__file__)
    pyblish.api.deregister_plugin_path(plugin_path)


def _discover_gui():
    """Return the most desirable of the currently registered GUIs"""

    # Prefer last registered
    guis = reversed(pyblish.api.registered_guis())

    for gui in guis:
        try:
            gui = __import__(gui)
        except (ImportError, AttributeError):
            continue
        else:
            return gui


def show():
    """Try showing the most desirable GUI."""
    app = _discover_gui()
    app.settings.WindowTitle = "Pyblish (photoshop)"
    app.show()


def setup():
    """Setup integration.

    Register plug-ins and integrate into the host

    """

    register_plugins()
    register_host()
    print("pyblish: Pyblish loaded successfully.")
