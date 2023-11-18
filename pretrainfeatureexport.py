import tensorflow
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import pickle
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input


model = ResNet50(weights='imagenet')

save_path = './modeltt.h5'
model.save(save_path)

with open("model.pkl",'wb') as files:
  pickle.dump(model,files)




model2 = VGG16(weights='imagenet')

save_path = './modeltt2.h5'
model2.save(save_path)

with open("model2.pkl",'wb') as files:
  pickle.dump(model2,files)


