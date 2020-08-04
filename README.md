[//]: # (Image References)

[image1]: ./dog-project/images/dog_4.jpg "Border collie" 
[image2]: ./dog-project/images/dog_5.jpg "Akita" 
[image3]: ./dog-project/images/dog_3.jpg "Hyena" 
[image4]: ./dog-project/images/cat.jpg "Cat"

# Dog Breed Detector

This is the capstone project for Data Scientist Nanodegree from Udacity. All of the necessairy code is provided in the jupyter notebook in the dog-project folder. If you want to run the code locally, please refer to the deployment instructions in the respective folder. I also developed a web app, which is deployed on Heroku https://my-dog-app.herokuapp.com/. You may experience problems on the server, so all the necessairy code for the local deployment of web app is provided in the folder dog-app.        

## Project Overview

The scope of the app is to classify dog breeds using pattern recognition. This may be a useful application for the fast and easy recognition of the specific dog breed from the provided pictures. For example, the breed recognition from pictures could be used to identify heritage of mixed dog breeds, which is interesting information for the current or future owners. In addition, the application may provide an opportunity for the targeted marketing for specific breed owners. App also recognizes humans and classifies them as the most similar dog breed. This is the funny part of this app!   

First, we want that our app succesfully detects and distuingishes humans and dogs on the given picture. Second, we want to detect one of 133 dog breeds on the picture. Therefore, the app has three main components:

- Detection of a human 
- Detection of a dog
- Classification of a specific dog breed

All three parts employ various pre-trained models based on connvolutional neural networks (CNNs) and are discussed in more detail in the methodology section. If you are interested in more technical information, please refer to the jupyter notebook in dog/project. 

## Data

The human dataset includes 13233 human images and small subset was used for the validation of the human and dog detection models. 

The dog dataset consists of 6680 training dog images, 835 validation dog images and 836 test dog images. The whole training and validation set were used for training of CNNs for dog breed classification, while test set was used to access model accuracy. Small subset of training set was used for the validation of the human and dog detection models. 

## Methodology

### Detection of the human

The app uses [OpenCVs](https://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html) implementation of Haar feature-based cascade classifiers to detect human faces in images. In this case, one of the pre-trained face detectors was used. This selected classifier detects humans on the pictures very well.  

### Detection of the dog

For the detection of dogs on pictures, pre-trained [ResNet-50](http://ethereon.github.io/netscope/#/gist/db945b393d40bfa26006) model was used. Used model performs perfectly on dog and human images. 

### Classification of a specific dog breed

The app CNNs created by transfer learning that can identify dog breed from images. The model uses the the pre-trained Xception as a fixed feature extractor, where the last convolutional output of [Xception](https://arxiv.org/abs/1610.02357) is fed as input to our model, which consist of two fully connected layers with relu and softmax activation function. The model has ~85% accuracy on the test set.  

## Results

The app was tested on a few selected images. Generally it seems to recognize dog breeds quite well. 

First, it correctly classifies following pictures as neither human nor dog:

![image3]

![image4]

Following images are correctly recognized as Border Collie and Akita. 

![image1]

![image2]

For humans, I tried few familiar faces, and it is fun to see the results (see the jupyter notebook for more results). However, I think it is actually quite hard to evaluate the results for humans since our perception is quite subjective. Although Lady Gaga definitely looks like poodle to me :-). What I noticed is that there is bias towards certain breeds such as Dachshund. Maybe Dachshund in general shares more underlying features with humans, and therefore larger number of human faces is detected as Dachshund.  

### Conclusion

Used models seem to work quite nicely on the pictures of decent quality. In the future, I would also consider using data augmentation to improve a models a bit further. In general, the transfer learning in this specific project resulted in models of good quality. 

Fun idea - It would be actually interesting too see small subset of dogs and their owners, and see if there is overlapping with the prediction from the app and real life. 
