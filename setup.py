# PyPI setup file

from setuptools import setup, find_packages
from iqgui.version import __version__
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

classifiers = [
    'Environment :: X11 Applications :: Qt',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3 :: Only',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Topic :: Scientific/Engineering :: Physics',
    'Intended Audience :: Science/Research',
]

setup(
    name='iqgui',
    packages=find_packages(),
    version=__version__,
    description='A qt-based GUI program that offers a graphical interface to visually inspect the data processed by the [iqtools library].',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='xaratustrah',
    url='https://github.com/xaratustrah/iqgui',  # use the URL to the github repo
    download_url='https://github.com/xaratustrah/iqgui/tarball/{}'.format(
        __version__),
    entry_points={
        'console_scripts': [
            'iqgui = iqgui.__main__:main'
        ]
    },
    license='GPLv3',
    keywords=['physics', 'atomic', 'mass', 'ion',
              'accelerators', 'spectral analysis'],  # arbitrary keywords
    classifiers=classifiers
)
