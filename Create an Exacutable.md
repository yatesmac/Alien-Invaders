# Creating the Executable


## PyInstaller
Use [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/index.html) to create the executable.Install PyInstaller from PyPI:

```shell script
pip install pyinstaller
```

After installing it, from inside the main game directory, simply run the command:

```shell script
pyinstaller --onefile --windowed alieninvaders.py
```

This will create an executable, using the default settings. This executable is placed inside a directory called `dist`. [This](https://realpython.com/pyinstaller-python/) guide contains further instruction on creating different binaries for Windows, MacOs or Linux.


## cx_Freeze

[cx_freeze](https://cx-freeze.readthedocs.io/en/latest/index.html) can also be used to create an executable.
Install cx_Freeze from PyPI:

```shell script
pip install cx_Freeze
```
Use the `setup.py` file for building the executable. Go to the directory main game directory and then run the command
```shell script
 python setup.py build
```
This will create a `build` directory inside the main game directory, and in it will be the executable - created using the default settings.. [This](https://cx-freeze.readthedocs.io/en/latest/distutils.html) guide and [this](https://cx-freeze.readthedocs.io/en/latest/faq.html) one contains further instruction on creating different binaries for Windows, MacOs or Linux.
