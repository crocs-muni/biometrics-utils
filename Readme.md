# Utilities for biometrics classes

A set of utilities for biometrics classes at the [Faculty of Informatics](https://www.fi.muni.cz/), [Masaryk University](https://muni.cz) based on deep learning and OpenCV.

## Usage

```
usage: detect_faces.py [-h] (-i IMAGE | -w WEBCAM) [-o OUTPUT] [-v] [-c CONFIDENCE] [-p PROTOTXT] [-m MODEL]

Detect faces using deep learning in OpenCV.

optional arguments:
  -h, --help            show this help message and exit
  -i IMAGE, --image IMAGE
                        path to input image
  -w WEBCAM, --webcam WEBCAM
                        webcam stream number (try 0, 1, 2, ...)
  -o OUTPUT, --output OUTPUT
                        image output directory
  -v, --verbose         display debugging output
  -c CONFIDENCE, --confidence CONFIDENCE
                        threshold to display face detections
  -p PROTOTXT, --prototxt PROTOTXT
                        path to Caffe 'deploy' prototxt file
  -m MODEL, --model MODEL
                        path to Caffe pre-trained model
```

## Installation

**Requirements**

* [Python](https://www.python.org/) (preferably version 3)
* python package [numpy](https://numpy.org/) (optimized library for mathematical operations)
* [opencv-python](https://pypi.org/project/opencv-python/) (unofficial pre-built CPU-only OpenCV packages for Python)
* [imutils](https://pypi.org/project/imutils/) (set of utility functions for OpenCV by Adrian Rosebrock)

_Note: Installig OpenCV separately is not necessary as opencv-python should ship with pre-build OpenCV._

**Setup**

- Install [Python](https://www.python.org/) (version 3) if you don't have it. Don't forget to install `pip`.
- Install python dependencies with `pip install --user -r requirements.txt` or use `make install` for convenience.
- You can test the installation with `python detect_faces.py --image images/example.jpg` or use `make demo` for convenience.

**Compatibility**

The setup was tested on Linux (Fedora 32) and Windows with local Python installation (running via PowerShell). Note that Windows WSL is not supported as `detect_faces.py` is a graphical application. MacOS was not tested.

## Sources

The unitities are based on the excellent tutorials at [pyImageSearch](https://www.pyimagesearch.com/) by Adrian Rosebrock.

* [Face detection with OpenCV and deep learning](https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/)
* [How to build a custom face recognition dataset](https://www.pyimagesearch.com/2018/06/11/how-to-build-a-custom-face-recognition-dataset/)
* [OpenCV Face Recognition](https://www.pyimagesearch.com/2018/09/24/opencv-face-recognition/)
