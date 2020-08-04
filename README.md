[//]: # (Image References)

[image1]: ./dog-project/images/dog_4.jpg "Border collie" 
[image2]: ./dog-project/images/dog_5.jpg "Akita" 
[image3]: ./dog-project/images/dog_3.jpg "Hyena" 
[image4]: ./dog-project/images/cat.jpg "Cat"

# Dog Breed Detector

This is the capstone project for Data Scientist Nanodegree from Udacity. All of the necessairy code is provided in the jupyter notebook in the dog-project folder. If you want to run the code locally, please refer to the deployment instructions (INSTRUCTIONS.md) in the respective folder. I also developed a web app, which is deployed on Heroku https://my-dog-app.herokuapp.com/. You may experience problems on the server, so all the necessairy code for the local deployment of web app is provided in the folder dog-app (INSTRUCTIONS_WEBAPP.md).        

## Project Overview

The scope of the app is to classify dog breeds on images using pattern recognition. This may be a useful application for the fast and easy recognition of the specific dog breed from the provided pictures. For example, the breed recognition from pictures could be used to identify heritage of mixed dog breeds, which is interesting information for the current or future owners. In addition, the application may provide an opportunity for the targeted marketing for specific breed owners. App also recognizes humans and classifies them as the most similar dog breed. This is the funny part of this app!   

First, we want that our app succesfully detects and distuingishes humans and dogs on the given picture. Second, we want to detect one of 133 dog breeds on the picture. Therefore, the app has three main components:

- Detection of a human 
- Detection of a dog
- Classification of a specific dog breed

All three parts employ various pre-trained models based on convolutional neural networks (CNNs) and are discussed in more detail in the methodology section. Models are evaluated based on their abilitiy to recognize human/dogs and classify specific dog breed. 

## Data

The human dataset includes 13233 human images. The dog dataset consists of 6680 training dog images, 835 validation dog images and 836 test dog images. 

## Methodology

### Image preprocessing
Prior to the model training, dog images have been preprocessed in the following way. Images were first resized to a square image that is  224×224  pixels. Next, images were converted to an array, which is then resized to a 4D tensor. Then, the RGB image is converted to BGR by reordering the channels. In the additional normalization step, the mean pixel (expressed in RGB as [103.939,116.779,123.68] and calculated from all pixels in all images in ImageNet) is subtracted from every pixel in each image.

### Detection of the human

The app uses pre-trained face detectors from [OpenCVs](https://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html). Two models based on either The Haar feature-based cascade classifiers and lbpcascade frontal-face classifier were validated on the small subset of human and dog images.     

### Detection of the dog

For the detection of dogs on pictures, pre-trained CNN [ResNet-50](http://ethereon.github.io/netscope/#/gist/db945b393d40bfa26006) model was used. Model was validated on the small subset of human and dog images.   

### Classification of a specific dog breed

The app uses CNNs to identify dog breed from images. Three different models were built and evaluated: simple CNN model built from scratch, model that uses transfer-learning and pre-trained [Xception](https://arxiv.org/abs/1610.02357) as a fixed feature extractor, and model that uses pre-trained [VGG-16] (https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/DogVGG16Data.npz) model as a fixed feature extractor. The whole training and validation set were used for training of CNNs for dog breed classification, while test set was used to access model accuracy. 

## Results

### Detection of human and dogs on images

Models based on The Haar feature-based cascade classifiers and lbpcascade frontal-face classifier had similar detection rate on the human (100% vs 88%) and dog (11.0% vs 1%) images. However, since The Haar feature-based cascade classifiers had better accuracy on the human images, it was selected for the implementation in the app. 

Pre-trained CNN ResNet-50 had perfect accuracy - it detected dog on all dog images, and it did not detect any dog on human images. 

 
Some of the examples are provided below. The selected models correctly classify following pictures as neither human nor dog:

![image3]

![image4]

### Classification of a specific dog breed

The model built from scratch exibited poor accuracy (10%). This is reasonable, since relatively simple network architecture with four convolutional layersa and two fully connected layers is unable to detect complex patterns in images. More complex models based on pretrained VGG-16 and Xception models excibited improved accuracy of 37% and 85%, respectively. The final model consisted of extracted feauters from pretrained Xception model and one average pooling layer and fully-connected output layer. Adding additional layers and dropout did not result in increased accuracy, therefore, this architecture was kept for the app.

With the final model, following images are correctly recognized as Border Collie and Akita. 

![image1]

![image2]

For humans, I tried few familiar faces, and it is fun to see the results (see the jupyter notebook for more results). However, I think it is actually quite hard to evaluate the results for humans since our perception is quite subjective. Although Lady Gaga definitely looks like poodle to me :-). What I noticed is that there is bias towards certain breeds such as Dachshund. Maybe Dachshund in general shares more underlying features with humans, and therefore larger number of human faces is detected as Dachshund. Fun idea - It would be actually interesting too see small subset of dogs and their owners, and see if there is overlapping with the prediction from the app and real life.  

### Conclusion

Deployed models seem to work quite nicely on the pictures of decent quality. However, there is some room for improvements for face detection and dog breed classification part. Face detection is not optimal if there is unusual skin tone (e.g. orange) or if there are some additional features (e.g. glasses). In the future, I would first consider using data augmentation to improve a models a bit further and trying additional model architectures for dog breed classification. 


