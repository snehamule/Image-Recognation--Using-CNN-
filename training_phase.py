import classifier as classifier
from PIL import Image


def train_cnn(training_data,validation_data):
    batch_size=16
    history= classifier.fit_generator(
            training_data,
            steps_per_epoch=2000 // batch_size,
            epochs=40,
            validation_data=validation_data,
            validation_steps=900 // batch_size)
    classifier.save_weights('save_weights.h5')  # always save your weights after training or during training