iqgui
============
<img src="https://raw.githubusercontent.com/xaratustrah/iqgui/master/rsrc/icon.png" width="128">

A qt-based GUI program that offers a graphical interface to visually inspect the data processed by the [iqtools library](https://github.com/xaratustrah/iqtools). Please refer to that library for more information and background on how the library works. This GUI tool also offers contrast manipulation and save/restore of plot configuration files. So if you create a plot for a publication, you can recreate the same plot later directly from the raw data.

![iq_suite](https://raw.githubusercontent.com/xaratustrah/iqgui/master/rsrc/screenshot.png)


## Installation and usage

#### Just running it

Alternatively you can just run the program as a python script. This code depends on the [iqtools library](https://github.com/xaratustrah/iqtools) library, so you need to [follow the installation instructions there](https://github.com/xaratustrah/iqtools#install--uninstall) first.

After installing the dependencies you can just run the program with:

    python ./iqgui.py

#### Installing it

alternatively you can install it using `pip`. Go to the directory and perform:

    pip install .

you can see the installed files by:

    pip show -f iqgui

you can uninstall it by:

    pip uninstall iqgui

#### Windows binaries

You can just use the program by using the binaries. In the release section of this repository there are binaries available for Windows. These have been tested also for Win-10.

## Acknowledgements
I am thankful to [@carlkl](https://github.com/carlkl) for his valuable help in making a stand alone binary under MS Windows and also for fruitful discussions and suggestions.
