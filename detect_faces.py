# import the necessary packages
from imutils.video import VideoStream
import numpy as np
import argparse
import time
import os
import cv2


# auxiliary functionm for logging
def log(logString):
    if args["verbose"]:
        print("[INFO] " + logString)


# process image data, detect faces, draw rectanles
def detectFaces(imageData):
    # construct an input blob for the image by resizing to a fixed 300x300 pixels and then normalizing it
    (h, w) = imageData.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(imageData, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the detections and predictions
    net.setInput(blob)
    detections = net.forward()
    finalDetections = []

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is greater than the minimum confidence
        if confidence < args["confidence"]:
            continue
        finalDetections.append(str(confidence))

        # compute the (x, y)-coordinates of the bounding box for the object
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # draw the bounding box of the face along with the associated probability
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(imageData, (startX, startY), (endX, endY), (0, 0, 255), 2)
        cv2.putText(imageData, text, (startX, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
    
    # return filtered detections
    return finalDetections


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser(description="Detect faces using deep learning in OpenCV.")
group = ap.add_mutually_exclusive_group(required=True)
group.add_argument("-i", "--image", help="path to input image")
group.add_argument("-w", "--webcam", type=int, help="webcam stream number (try 0, 1, 2, ...)")
ap.add_argument("-o", "--output", default="images", help="image output directory")
ap.add_argument("-v", "--verbose", action='store_true', help="display debugging output")
ap.add_argument("-c", "--confidence", type=float, default=0.2, help="threshold to display face detections")
ap.add_argument("-p", "--prototxt", default="models/deploy.prototxt.txt", help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", default="models/res10_300x300_ssd_iter_140000.caffemodel", help="path to Caffe pre-trained model")
args = vars(ap.parse_args())

# load our serialized model from disk
log("Loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

if args["image"] is not None:
    # load the input image and construct an input blob for the image by resizing to a fixed 300x300 pixels and then normalizing it
    log("Loading input image ...")
    image = cv2.imread(args["image"])

    # detect faces, draw rectangles, return filtered confidence numbers
    detections = detectFaces(image)

    # draw instructiuons
    cv2.putText(image, "[any key] close preview", (10, 25), cv2.FONT_HERSHEY_PLAIN, 1.3, (0, 0, 255), 2)

    # show the output image, put confidence in CLI
    cv2.imshow("Output", image)
    print(args["image"] + "," + ','.join(detections))
    cv2.waitKey(0)

    # save image with detections
    filepath, extension = os.path.splitext(args["image"])
    pathDetected = filepath + "-faces" + extension
    log("Saving image " + pathDetected + " ...")
    cv2.imwrite(pathDetected, image)

elif args["webcam"] is not None:
    # initialize the video stream and allow the cammera sensor to warmup
    log("Starting video stream ...")
    vs = VideoStream(src=args["webcam"]).start()
    time.sleep(1.0)
    total = 0

    # loop over the frames from the video stream
    while True:
        # grab the frame from the threaded video stream, make a copy for saving
        frame = vs.read()
        orig = frame.copy()

        # detect faces, draw rectangles, return filtered confidence numbers
        detections = detectFaces(frame)

        # draw instructiuons
        cv2.putText(frame, "[w] write frame to disk", (10, 25), cv2.FONT_HERSHEY_PLAIN, 1.3, (0, 0, 255), 2)
        cv2.putText(frame, "[q] quit video stream", (10, 50), cv2.FONT_HERSHEY_PLAIN, 1.3, (0, 0, 255), 2)

        # show the output frame
        cv2.imshow("Webcam " + str(args["webcam"]) + " stream", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `w` key was pressed, write the original and adjusted frame to disk, put confidence in CLI
        if key == ord("w"):
            total += 1
            totalString = "{}".format(str(total).zfill(3))
            print(totalString + ".jpg," + ','.join(detections))
            pathOriginal = os.path.sep.join([args["output"], totalString + ".jpg"])
            pathDetected = os.path.sep.join([args["output"], totalString + "-faces.jpg"])
            log("Saving images " + pathOriginal + ", " + pathDetected + " ...")
            cv2.imwrite(pathOriginal, orig)
            cv2.imwrite(pathDetected, frame)

        # if the `q` key was pressed, break from the loop
        elif key == ord("q"):
            break

    # do a bit of cleanup
    log("Closing webcam stream ...")
    cv2.destroyAllWindows()
    vs.stop()
