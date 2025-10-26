Importing Libraries:

import tensorflow as tf 
import keras 
import os 
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
from PIL import ImageFile 
from tensorflow.keras.utils import to_categorical 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix 
from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from tensorflow.keras.applications.resnet50 import ResNet50 
from keras import Model, layers 
from keras.models import Sequential 
from tensorflow.kera import s.optimizers import SGD 
from keras.layers import GlobalMaxPooling2D, GlobalAveragePooling2D, Dropout, Dense, Input, Conv2D, MaxPooling2D, Flatten,MaxPooling3D 
