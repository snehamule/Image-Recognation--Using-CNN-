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
	refer steps from [windows python installation steps](https://docs.python.org/3/using/windows.html).
	

## Check python version:
python -version


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
Download Flower Dataset from kaggle [Flower Datset](https://www.kaggle.com/alxmamaev/flowers-recognition)
         Fruits Dataset from kaggle [Fruits Datset] (https://www.kaggle.com/moltean/fruits/discussion/54011)
         Natural images from kaggle [Natural Images Datset] (https://www.kaggle.com/prasunroy/natural-images)
         Cats-Dog Dataset from kaggle [Cats-Dogs Datset] (https://www.kaggle.com/c/dogs-vs-cats)

## Parameter Selected:<br />
image_size =150
class_mode= Categorical
batch_size =16
Activation function = relu
Dropout =0.5
Fully connected layer activation = softmax
optimizer=adam
loss= categorical_crossentropy
metrics= accuracy

## Run program : <br />
1. Download code from git  using  git clone .
2. Place downloaded dataset files in the same folder
3. For Process the Data run command 
```
	python process_data.py
```	
4. To run backpropogation algorithm, run command 
```
	python backPropogation_algorithm py
```
5. To run same program using scikit learn :
```
     python scitkit_learn_backpropogation_algo.py

```
