# Drowsiness Detection

- Detecta whether a person is drowsy or awake in real time using the device's webcam.
- Uses the YOLOv5 model as the base of the project for face detection. A custom data set of images was created and labelled (awake or drowsy) manually using LabelImg.
- The YOLOv5 model is trained on the custom data set using Pytorch. 
- The custom trained model is loaded and with the help of OpenCV can detect drowsiness in real time.

## Screenshots

![App Screenshots](https://raw.githubusercontent.com/vishnusingh-12/drowsiness-detection/master/readme/awake.PNG)
![App Screenshots](https://raw.githubusercontent.com/vishnusingh-12/drowsiness-detection/master/readme/drowsy.PNG)



## Deployment
<pre>git clone  https://github.com/vishnusingh-12/drowsiness-detection
cd drowsiness-detetcion
pip install -r requirements.txt
python app.py </pre>
Instead of python app.py you can also double click on app.py and wait for the application to run.

The model uses Pytorch and cuda 11.8 for training the model. The Drwosiness_detection.ipynb file has all the information to train your own custom model using CPU as well.
To run app.py (my custom model) torch and  opencv are required after cloning the repo.


## Technologies
<img src="https://raw.githubusercontent.com/vishnusingh-12/drowsiness-detection/master/readme/techs.PNG">

## Support

For support, contact me:

[<img src="https://img.icons8.com/color/48/000000/gmail.png" alt="Gmail" width="30" height="30">](mailto:vishnusingh1995@gmail.com)
&nbsp;&nbsp;&nbsp;
[<img src="https://img.icons8.com/color/48/000000/instagram-new.png" alt="Instagram" width="30" height="30">](https://www.instagram.com/vishnusingh12/)
&nbsp;&nbsp;&nbsp;
[<img src="https://img.icons8.com/ios-filled/50/000000/github.png" alt="GitHub" width="30" height="30">](https://github.com/vishnusingh-12)
&nbsp;&nbsp;&nbsp;
[<img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn" width="30" height="30">](https://www.linkedin.com/in/singh-vishnu)

