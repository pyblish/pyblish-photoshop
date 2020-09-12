<p align="center">
<img src="https://imgur.com/kn8wOQj.png" alt="logo"></a>
</p>

pyblish-photoshop
=================
Pyblish integration for Adobe Photoshop cs6-2020 (Window only).

What is included?
A set of common plug-ins and functions shared across other integrations - such as getting the current working file. It also visually integrates Pyblish into the File-menu for easy access.
- Common [plug-ins](https://github.com/pyblish/pyblish-photoshop/tree/master/pyblish_photoshop/plugins)
- Common [command line](https://github.com/pyblish/pyblish-photoshop/blob/master/pyblish_photoshop/cli.py)

<br>
<br>
<br>

Installation
------------
Via pip install `pyblish-photoshop` will be installing all depends packages.

```cmd
pip install pyblish-photoshop
```

Install pyblish menu into Photoshop
```cmd
pyblish-photoshop install --app-dir "your/photoshop/install/localtion"
```
For example:
```cmd
pyblish-photoshop install --app-dir "C:\Program Files\Adobe\Adobe Photoshop 2020"
```

Usage
-----
```cmd
pyblish-photoshop --help
```
```cmd
Usage: pyblish-photoshop [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  gui      Show Pyblish GUI, Default is to use "pyblish_lite".
  install  Install pyblish menu into Photoshop.
```

Launch UI
---------
In Photoshop go to the `Filter` menu and you will see the `pyblish` menu.

<img src="https://imgur.com/LhrBTVU.png" alt="UI"></a>
