# Face detection utility

A set of utilities for face detection for the biometrics classes at the [Faculty of Informatics](https://www.fi.muni.cz/), [Masaryk University](https://muni.cz) based on deep learning and OpenCV.

## Usage

Use the python script `detect_faces.py` to detect faces using deep learning in OpenCV.

```bash
python3 detect_faces.py [-h] (-i IMAGE | -w WEBCAM)
                        [-o OUTPUT] [-v] [-c CONFIDENCE]
                        [-p PROTOTXT] [-m MODEL]
```

Optional arguments:

* `-h` / `--help`  
  show this help message and exit
* `-i IMAGE` / `--image IMAGE`  
  path to input image
* `-w WEBCAM` / `--webcam WEBCAM`  
  webcam stream number (try 0, 1, 2, ...)
* `-o OUTPUT` / `--output OUTPUT`  
  image output directory
* `-v` / `--verbose`  
  display debugging output
* `-c CONFIDENCE` / `--confidence CONFIDENCE`  
  threshold to display face detections (default: 0.2)
* `-p PROTOTXT` / `--prototxt PROTOTXT`  
  path to a different Caffe 'deploy' prototxt file
* `-m MODEL` / `--model MODEL`  
  path to a different Caffe pre-trained model

## Installation

### Requirements

* [Python](https://www.python.org/) (preferably version 3)
* python package [numpy](https://numpy.org/) (optimized library for mathematical operations)
* [opencv-python](https://pypi.org/project/opencv-python/) (unofficial pre-built CPU-only OpenCV packages for Python)
* [imutils](https://pypi.org/project/imutils/) (set of utility functions for OpenCV by Adrian Rosebrock)

_Note: Installing OpenCV separately is not necessary as opencv-python should ship with pre-build OpenCV._

### Setup

1. Install [Python](https://www.python.org/) (version 3) if you don't have it. Don't forget to install `pip`.
2. Create a virtual environment `virt` with `python3 -m venv virt`. Activate it `. virt/bin/activate` (assuming Bash).
3. Install Python dependencies with `pip3 install -r requirements.txt` or use `make install` for convenience.
4. You can test the installation with `python3 detect_faces.py --image images/example.jpg` or use `make demo` for convenience.

### Compatibility

The setup was tested on Linux (Fedora 33, Ubuntu 20.04), MacOS and Windows with local Python installation (running via PowerShell). Note that Windows WSL is not recommended as `detect_faces.py` is a graphical application. Use within a virtual machine is possible, though extra configuration may be necessary to get webcams working.

## Working principles

The face detector used by the utility uses the technique of Haar Cascades. A nice brief explanation can be found directly in the [OpenCV-Python Tutorials](https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html). Haar Cascades are a machine learning approach based on comparing pixel intensities in adjacent regions. For example, consider the image below. Top row shows two good features. The first feature focuses on the region of the eyes being often darker than the region of the nose and cheeks. The second feature relies on the eyes being darker than the bridge of the nose.

![Exemplary Haar Cascades features](https://docs.opencv.org/4.x/haar.png)

To find out which features work well, we use machine learning: we induce (train) good features from a lot of images classified manually. After having trained the set of features, face detection works by "brute-forcing" the regions on all possible location of the image (a very nice slowed illustration of the process can be seen [in this video](https://vimeo.com/12774628)). There are some more tricks to make this more efficient but those are not that important here.

The trained detector is pretty versatile – and therefore comes bundled with OpenCV. That means you don't need to do any training/machine learning yourself, just use the model available in OpenCV.

## Sources

The utilities are based on the excellent tutorials at [pyImageSearch](https://www.pyimagesearch.com/) by Adrian Rosebrock.

* [Face detection with OpenCV and deep learning](https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/)
* [How to build a custom face recognition dataset](https://www.pyimagesearch.com/2018/06/11/how-to-build-a-custom-face-recognition-dataset/)
* [OpenCV Face Recognition](https://www.pyimagesearch.com/2018/09/24/opencv-face-recognition/)
