from cnn import  create_convolutional_netowork
from data_generator import  traing_data_generator,testing_data_generator
from data_process import process_data
from training_phase import  train_cnn
from testing_phase import test_cnn

create_convolutional_netowork()
training_data,validation_data = process_data('Training_Dataset'
             ,'Validation_Data',150,'categorical')

train_cnn(training_data,validation_data)
#test_cnn(Skip_lable=False): Pass True if do not want to display lable
test_cnn()
