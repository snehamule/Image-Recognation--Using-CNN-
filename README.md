# Image Recognation using Convolutional Neural Network

This project is aimed to indentify cat,dog,horse,car,motorbike,Fruit,Flower,human images using convolutional neural network.
Trained neural network with 10K images, and also considered different angles for each image. So, trained neural network with 200K (20*10K ) imgaes.<br />

Accuracy on testing data is 98.78%.<br />
To avoid overfitting used validation set and dropout = 0.5<br />

## Convolutional neural network:
Convolutional neural network:
A convolutional neural network contains several layers, first convolutional layer, then
pooling layer then activation layer.
Convolution neural network extract features from the images and learn about the image.
### Convolutional layer:
To understand convolutional layer, consider 5*5 image and take 2*2 matrix which is
called filter slide it that image. When we slide filter from the image then a matrix of the
image multiply with filter, and summation of it produce a single number for a particular
window of image and filter.

### Pooling Layer:
There are commonly two types of pooling, max pooling, and average pooling. Max pooling
takes the large value of the window of the image which is cover by the filter. Average
pooling takes the average value of window of the image which is cover by the filter
### Activation layer:
The activation function is similar to activation function other neural networks use. When
the value passes through the function, it squeezes the value according to the activation
function. For instance sigmoid activation function squeezes between 1 or 0, tanh
activation function squeezes value between 1 and -1, relu activation function squeezes
value 1 or 0.<br />
![Alt text](https://www.google.com/search?rlz=1C5CHFA_enUS775US775&biw=1440&bih=790&tbm=isch&sa=1&ei=OkmkW7PsHdGt0PEP_vGBmA4&q=convolutional+neural+network+architecture&oq=convolutional+neural+network+arc&gs_l=img.3.0.0l2j0i24l8.1861.2284..3263...0.0..0.60.168.3......1....1..gws-wiz-img.BuDVoav1WCk#imgrc=RSyJWTrg8ZkGDM: "Optional title")
![Convolution Neural Network Diagram] (https://www.google.com/search?rlz=1C5CHFA_enUS775US775&biw=1440&bih=790&tbm=isch&sa=1&ei=OkmkW7PsHdGt0PEP_vGBmA4&q=convolutional+neural+network+architecture&oq=convolutional+neural+network+arc&gs_l=img.3.0.0l2j0i24l8.1861.2284..3263...0.0..0.60.168.3......1....1..gws-wiz-img.BuDVoav1WCk#imgrc=RSyJWTrg8ZkGDM:)


## Technology / libraries used: <br />
Python, Keras,Numpy, matplotlib

## Setup required:<br />
Python version: 3 or greater<br />
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
This Image recognation application used following Dataset.<br />
Flower Dataset from kaggle [Flower Datset](https://www.kaggle.com/alxmamaev/flowers-recognition)<br />
Fruits Dataset from kaggle [Fruits Datset](https://www.kaggle.com/moltean/fruits/discussion/54011)<br />
Natural images from kaggle [Natural Images Datset](https://www.kaggle.com/prasunroy/natural-images)<br />
Cats-Dogs Dataset from kaggle [Cats-Dogs Datset](https://www.kaggle.com/c/dogs-vs-cats)<br />


## Parameter Selected:<br />
* Image_size =150<br />
* Class_mode= Categorical<br />
* Batch_size =16<br />
* Activation function = relu<br />
* Dropout =0.5<br />
* Fully connected layer activation = softmax<br />
* Optimizer=adam<br />
* Loss= categorical_crossentropy<br />
* Metrics= accuracy<br />

## Run program : <br />
1. Download code from git  using  git clone.
2. Place downloaded dataset files in the same folder
3. To run application, run command 
```
	python image_recognation_cnn.py py
```
