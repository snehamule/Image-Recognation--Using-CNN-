# Image Recognation using Convolutional Neural Network

This project is aimed to indentify cat,dog,horse,car,motorbike,Fruit,Flower,human images using convolutional neural network.
Trained neural network with 10K images, and also considered different angles for each image. So, trained neural network with 200K (20*10K ) imgaes.<br />

Accuracy on testing data is 98.78%.<br />
To avoid overfitting used validation set and dropout = 0.5<br />


## Technology / libraries used: <br />
Python, Keras,Numpy, matplotlib

## Setup required:<br />
python version: 3 or greater<br />
Libraries : Keras, Numpy,matplotlib


## Install python <br />
If python is not installed then need to install python:<br />
<br />
**For  osx operating system (mac)**<br />
	python get-pip.py 

**For windows operating system**<br />
	refer steps from [windows python installation steps](https://docs.python.org/3/using/windows.html).<br />
	

## Check python version:
python -version<br />


## Install Libraries<br /> 

**For  osx operating system (mac)**<br />
* Install Numpy : pip install numpy<br />
* Install  Keras : pip install keras<br />
* Install  matplotlib : pip install matplotlib<br />


**For windows operating system**<br />
* Install numpy : pip install numpy<br />
* Install Keras : pip install keras<br />
* Install  matplotlib: pip install matplotlib<br />


## Dataset Download :<br />
This recommendation system use  Book-Crossing Dataset.
Download Flower Dataset from kaggle [Flower Datset](https://www.kaggle.com/alxmamaev/flowers-recognition)<br />
         Fruits Dataset from kaggle [Fruits Datset] (https://www.kaggle.com/moltean/fruits/discussion/54011)<br />
         Natural images from kaggle [Natural Images Datset] (https://www.kaggle.com/prasunroy/natural-images)<br />
         Cats-Dog Dataset from kaggle [Cats-Dogs Datset] (https://www.kaggle.com/c/dogs-vs-cats)<br />

## Parameter Selected:<br />
* image_size =150<br />
* class_mode= Categorical<br />
* batch_size =16<br />
* Activation function = relu<br />
* Dropout =0.5<br />
* Fully connected layer activation = softmax<br />
* optimizer=adam<br />
* loss= categorical_crossentropy<br />
* metrics= accuracy<br />

## Run program : <br />
1. Download code from git  using  git clone.
2. Place downloaded dataset files in the same folder
3. To run application, run command 
```
	python image_recognation_cnn.py py
```
