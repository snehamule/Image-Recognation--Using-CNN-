from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
def traing_data_generator():
    traing_data_generator = ImageDataGenerator(
        shear_range=0.2,
        zoom_range=0.3,
        rescale=1. / 255,
        horizontal_flip=True)

    return traing_data_generator


def testing_data_generator():
    testing_data_generator = ImageDataGenerator(rescale=1. / 255)
    return testing_data_generator

def visualize_generated_image(image_path):
    img = load_img(image_path)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    train_datagen=traing_data_generator()
    i=0
    for batch in train_datagen.flow(x, batch_size=1,
                          save_to_dir='/Convolution_NN_Project/Preview', save_prefix='cat', save_format='jpeg'):
        i += 1
        if i > 20:
            break  # otherwise the generator would loop indefinitely
