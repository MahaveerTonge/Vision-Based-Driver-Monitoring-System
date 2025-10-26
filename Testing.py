Importing Libraries: 
import os 
import pandas as pd 
import numpy as np 
from PIL import Image 
import cv2 


Load saved Model: 
BASE_DIR = "D:/Project code/Final" 
BASE_MODEL_PATH = BASE_DIR 
BEST_MODEL = os.path.join(BASE_MODEL_PATH,"Driver_behaviour_resnet1.h5") 
model = load_model(BEST_MODEL) 
Prediction of Image: 
def path_to_tensor(img_path): 
img = np.asarray(img_path) 
img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC) 
x = image.img_to_array(img) 
return np.expand_dims(x, axis=0) 
def return_prediction(filename): 
ImageFile.LOAD_TRUNCATED_IMAGES = True 
print(type(filename)) 
test_tensors = path_to_tensor(filename).astype('float32')/255 - 0.5 
ypred_test = model.predict(test_tensors,verbose=1) 
ypred_class = np.argmax(ypred_test,axis=1) 
print(ypred_class) 
id_labels = dict() 
for class_name,idx in labels_id.items(): 
id_labels[idx] = class_name 
print(id_labels) 
ypred_class = int(ypred_class) 
res = id_labels[ypred_class] 
def process(path): 
image = Image.open(path) 
res=return_prediction(image) 
print("PREDICTED RESULT==",res) 
return res 
res=pred.process(path) 
finalcolor="" 
if res=="SAFE DRIVING": 
finalcolor=color 
pflag=False 
else: 
finalcolor=color1 
pflag=True 
playsound("alarm1.wav") 
msg1="PLEASE PAY ATTENTION AS YOUR CURRENT BEHAVIOUR "+str(res)+" IS UNSAFE" 
engine.setProperty('rate',125) 
engine.say(msg1) 
engine.runAndWait() 
msg1="" 
img=cv2.imread(path) 
cv2.putText(img,str(res),(450,100),cv2.FONT_HERSHEY_SIMPLEX, 0.45, finalcolor, 2) 
cv2.imshow("OUTPUT IMAGE",img) 
print("FLAG==",pflag) 
if pflag: 
loc=g.get_loc() 
msg=str(res)+" AT "+"https://www.google.co.in/maps/place/"+loc 
tes.process(msg,"7619533826") 
