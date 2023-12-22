# Drowsiness Detection

- Detecta whether a person is drowsy or awake in real time using the device's webcam.
- Uses the YOLOv5 model as the base of the project for face detection. A custom data set of images was created and labelled (awake or drowsy) manually using LabelImg.
- The YOLOv5 model is trained on the custom data set using Pytorch. 
- The custom trained model is loaded and with the help of OpenCV can detect drowsiness in real time.

## Screenshots

![App Screenshots](https://raw.githubusercontent.com/vishnusingh-12/drowsiness-detection/master/awake.PNG)
![App Screenshots](https://raw.githubusercontent.com/vishnusingh-12/drowsiness-detection/master/drowsy.PNG)



## Documentation

git clone  https://github.com/vishnusingh-12/drowsiness-detection

cd drowsiness-detetcion

pip install -r requirements.txt

python app.py (or just double click app.py to run the application)

The model uses Pytorch and cuda 11.8 for training the model. The Drwosiness_detection.ipynb file has all the information to train your own custom model using CPU as well.
To run app.py (my custom model) torch and  opencv are required after cloning the repo.


## Technologies


