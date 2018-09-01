from data_generator import traing_data_generator,testing_data_generator

def process_data(training_data_path,validation_data_path,image_size=150,classification_mode='binary',batch_size=16):
    traing_data_generate = traing_data_generator()
    testing_data_generate= testing_data_generator()
    #visualize_generated_image('Training_Data/Cat/cat.0.jpg')

    training_data = traing_data_generate.flow_from_directory(
        training_data_path ,target_size=(image_size, image_size),
        batch_size=batch_size,class_mode=classification_mode)


    validation_data = testing_data_generate.flow_from_directory(
       validation_data_path,target_size=(image_size, image_size),
        batch_size=batch_size,class_mode=classification_mode)
    return training_data,validation_data