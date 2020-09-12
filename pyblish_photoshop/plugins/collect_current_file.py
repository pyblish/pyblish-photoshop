import pyblish.api


class CollectPhotoshopCurrentFile(pyblish.api.ContextPlugin):
    """Inject the current active document file path into context."""

    order = pyblish.api.CollectorOrder - 0.5
    label = "Photoshop current active document"

    hosts = ['photoshop']
    version = (0, 1, 0)

    def process(self, context):
        """Inject the current working file"""
        import os
        from photoshop.api import Application
        app = Application()

        current_file = app.activeDocument.fullName
        self.log.info(current_file)
        normalised = os.path.normpath(current_file)
        context.set_data('currentFile', value=normalised)
