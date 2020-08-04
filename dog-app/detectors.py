from extract_bottleneck_features import extract_Xception
import re
import numpy as np
import cv2  

from keras.preprocessing import image 
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.models import load_model


def path_to_tensor(img_path):
    
    '''
    Function takes a string-valued file path to 
    a color image as input and returns a 4D tensor suitable for supplying 
    to a Keras CNN.
        Parameters:
            img_path (string): file path to a color image
        Returns:
            (numpy array): 4D tensor for the input image
    '''
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def face_detector(img_path):
    '''
    Function returns "True" if face is detected in image stored at img_path. 
        Parameters:
            img_path (string): path to the image
        Returns: 
        (boolean):  "True" if face is detected, "False" otherwise
    '''
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0

def ResNet50_predict_labels(img_path):
    '''
    Function that returns prediction for the input image according to the 
    one of 1000 categories in ResNet50.
    Paramteres:
        img_path(string): path to the input image
    Returns:
        (integer): integer corresponding to the model's predicted object
        class 
    '''
    ResNet50_model = ResNet50(weights="imagenet")
    # returns prediction vector for image located at img_path   
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))

def dog_detector(img_path):
    '''
    Function returns "True" if dog is detected in image stored at img_path. 
        Parameters:
            img_path (string): path to the image
        Returns: 
        (boolean):  "True" if dog is detected, "False" otherwise
    '''
    prediction = ResNet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151)) 


def get_dog_names ():
    '''
    Function that returns dog breed names from the saved file
    '''
    # define an empty list
    dog_names = []

    # open file and read the content in a list
    with open('dog_names.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]

            # add item to the list
            dog_names.append(currentPlace)
    
    return dog_names

def predict_breed(img_path):
    '''
    Function that takes a path to an image as input
    and returns the dog breed that is predicted by the model.
        Paramteres:
            img_path (string): path to the input image
        Returns:
            (string): predicted dog breed
    '''
    #Load model
    Xception_model = load_model("saved_models/Xception_model")
    # extract bottleneck features
    bottleneck_feature = extract_Xception(path_to_tensor(img_path))
    # obtain predicted vector
    predicted_vector = Xception_model.predict(bottleneck_feature)
    #get dog breed names
    dog_names = get_dog_names()
    # assign dog breed that is predicted by the model  
    dog_breed = dog_names[np.argmax(predicted_vector)]
    #return the predicted dog breed
    return dog_breed[re.search('\.', dog_breed).span()[1]:]

def dog_breed_detector(img_path):
    '''
    Function to detect dog breed for input image of human or dog. It returns an error if none.
        Parameters:
            img_path (string): input image path
        Returns:
            None
    '''
    
    if face_detector(img_path) > 0:
        return(predict_breed(img_path))
    
    elif dog_detector(img_path) > 0:
        return(predict_breed(img_path))
    
    else:
        return("Please provide additional photo. Neither human or dog are detected")