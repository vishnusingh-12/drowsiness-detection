import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt
import uuid
import os
import time

# loading the trained model
# the model results are stored in the root directory in 'yolov5/runs/train/exp/weights/last.pt'

model=torch.hub.load(repo_or_dir='yolov5',model='custom',path='yolov5/runs/train/exp/weights/last.pt', force_reload=True,source='local')

# Realtime Detection  using opencv

# accesing the machine webcam
cap = cv2.VideoCapture(0)

# checking if the webcam is open or not
while cap.isOpened():

    # gives a return value and a frame (captured image)
    ret, frame = cap.read()

    # Make detections using model
    results = model(frame)

    # showing the results for each frame
    cv2.imshow('YOLO', np.squeeze(results.render()))

    # if 'q' key is pressed loop breaks
    key = cv2.waitKey(10)
    if key == ord('q') or key == 27:  # 'q' key or Esc key
        break
        # if window is closed, exit the loop
    if cv2.getWindowProperty('YOLO', cv2.WND_PROP_VISIBLE) < 1:
        break
# release the machine webcam
cap.release()

# destroy all opened windows
cv2.destroyAllWindows()