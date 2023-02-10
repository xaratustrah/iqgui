# iqgui

<img src="https://raw.githubusercontent.com/xaratustrah/iqgui/master/iqgui/rsrc/icon.png" width="128">

A qt-based GUI program that offers a graphical interface to visually inspect the data processed by the [iqtools library](https://github.com/xaratustrah/iqtools). Please refer to that library for more information and background on how the library works. This GUI tool also offers contrast manipulation and save/restore of plot configuration files. So if you create a plot for a publication, you can recreate the same plot later directly from the raw data.

![iq_suite](https://raw.githubusercontent.com/xaratustrah/iqgui/master/iqgui/rsrc/screenshot.png)


## Installation and usage

#### Requirements

This library requires the installation of [iqtools library](https://github.com/xaratustrah/iqtools). Please follow the instruction there. Other than that, you still need PyQT which you can install like this:

    conda install --channel=conda-forge pyqt

#### Installation

You can install the package using `pip` if you like:

    cd iqgui
    pip install .

Alternatively you can just run the program as a python module:

    python -m iqgui


#### Windows binaries

You can just use the program by using the binaries. In the release section of this repository there are binaries available for Windows. These have been tested also for Win-10.


## Acknowledgements
I am thankful to [@carlkl](https://github.com/carlkl) for his valuable help in making a stand alone binary under MS Windows and also for fruitful discussions and suggestions.


## Citation for publications

If you are using this code in your publications, please refer to [DOI:10.5281/zenodo.7615693](https://doi.org/10.5281/zenodo.7615693) for citation

