iqgui
============
<img src="https://raw.githubusercontent.com/xaratustrah/iqgui/master/rsrc/icon.png" width="128">

A qt-based GUI program that offers a graphical interface to visually inspect the data processed by the [iqtools library](https://github.com/xaratustrah/iqtools). Please refer to that library for more information and background on how the library works. This GUI tool also offers contrast manipulation and save/restore of plot configuration files. So if you create a plot for a publication, you can recreate the same plot later directly from the raw data.

![iq_suite](https://raw.githubusercontent.com/xaratustrah/iqgui/master/rsrc/screenshot.png)


## Installation and usage

More general info on python installation under Win and OSX can be found on this [gist](https://gist.github.com/xaratustrah/4efc5001f1bbcce47e02e2343ba29b87). Just remember to install missing packages, like `pyTDMS`.

#### Windows Binary

In the release section I put some compiled versions for windows.

#### Building OSX App

After making sure the run time version stars without any problems, you may like to build an app. You need to use `py2app`:

    python setup_osx.py py2app

Still I encountered a couple of errors which I describe here. I needed to modify this file:

    /opt/local/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/py2app/recipes/pyopengl.py

open it and change `file` to `open`. The after consulting [this post](http://stackoverflow.com/a/32750895/5177935) this file needed to be changed:

    /opt/local/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/macholib/dyld.py

where each instance of `loader_path` was changed to `loader`.


## Acknowledgements
I am thankful to [@carlkl](https://github.com/carlkl) for his valuable help in making a stand alone binary under MS Windows and also for fruitful discussions and suggestions.
