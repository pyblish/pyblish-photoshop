<p align="center">
<img src="https://imgur.com/lahtkVx.png" alt="logo"></a>
</p>

pyblish-photoshop
=================
Pyblish for Photoshop

Pyblish integration for Adobe Photoshop cs6-2020.


install
-------

Use pip.
```cmd
pip install pyblish-photoshop
```

Use git.
```cmd
git clone https://github.com/pyblish/pyblish-photoshop 
```

Install pyblish menu into Photoshop
```cmd
pyblish-photoshop install --app-dir "your/photoshop/install/localtion"
```
For example:
```cmd
pyblish-photoshop install --app-dir "C:\Program Files\Adobe\Adobe Photoshop 2020"
```

usage:
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
