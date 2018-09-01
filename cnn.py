from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D,Convolution2D
from keras.layers import Activation, Dropout, Flatten, Dense


def create_convolutional_netowork() :
    img_size=150
    classifier = Sequential()
    classifier.add(Conv2D(32, (3, 3), input_shape=(img_size, img_size, 3)))
    classifier.add(Activation('relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    classifier.add(Conv2D(32, (3, 3)))
    classifier.add(Activation('relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    classifier.add(Conv2D(32, (3, 3)))
    classifier.add(Activation('relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    classifier.add(Flatten())
    classifier.add(Dense(64))
    classifier.add(Activation('relu'))
    classifier.add(Dropout(0.5))
    classifier.add(Dense(output_dim=8))
    classifier.add(Activation("softmax"))

    classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
