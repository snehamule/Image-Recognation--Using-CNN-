import numpy as np
import classifier as classifier
from data_generator import  testing_data_generator


catagory_names={0:'airplane',1:'car',2:'cat',3:'dog',4:'flower',5:'fruit',6:'motorbike',7:'person'}
def test_cnn(skip_lables=False):
    testing_data_generate = testing_data_generator()

    testing_data = testing_data_generate.flow_from_directory(
        'Test_data', target_size=(150, 150),
        batch_size=16, class_mode=None)

    # test_generator.reset() #Necessary to force it to start from beginning
    Y_pred = classifier.predict_generator(testing_data)
    y_pred = np.argmax(Y_pred, axis=-1)
    predictions = [catagory_names[k] for k in y_pred]
    print(predictions if skip_lables == False else y_pred)