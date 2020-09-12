# Import built-in modules
import os

# Import third-party modules
import click
import pyblish.api

# Import local modules
from pyblish_photoshop import app


@click.group()
def cli():
    pass


@cli.command("gui", help='Show Pyblish GUI, Default is to use '
                         '"pyblish_lite".')
@click.option("package", "--register-gui",
              type=click.Choice(["pyblish_qml", "pyblish_lite"]),
              default="pyblish_lite")
def pyblish_gui(package):
    pyblish.api.register_gui(package)
    app.setup()
    app.show()


@cli.command("install", help="Install pyblish menu into Photoshop.")
@click.option("install_folder", "--app-dir", type=click.Path(exists=True))
def install_script(install_folder):
    template = """
/*
// BEGIN__HARVEST_EXCEPTION_ZSTRING

<javascriptresource>
<name>pyblish</name>
<about>Pyblish for Photoshop.</about>
<category>photoshop</category>
<menu>filter</menu>
</javascriptresource>


// END__HARVEST_EXCEPTION_ZSTRING

   The item tagged "name" specifies the localized name or ZString that will be displayed in the menu
   The item tagged "menu" specifies the menu in which the command will appear: generate, automate, scripts, or filter
   The item tagged "enableinfo" specifies the conditions under which the command will be enabled. Too complex to describe here; see plugin sdk. Should usually just be "true", and your command should report a user-comprehensible error when it can't handle things. The problem with disabling the command when it's unsuitable is that there's no hint to the user as to why a command is disabled.
   The item tagged "about" specifies the localized text or ZString to be displayed in the about box for the plugin. Optional.
   The item tagged "eventid" needs to be a guaranteed unique string for your plugin. Usually generated with a UUID generator like uuidgen on MacOS
*/
{

app.system("start pyblish-photoshop gui")

}    
"""
    script_path = os.path.join(install_folder, "Presets", "Scripts",
                               "pyblish.jsx")
    with open(script_path, "w") as file_obj:
        file_obj.write(template)
    click.echo("Install Done: {}".format(script_path))
