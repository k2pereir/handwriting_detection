import tensorflow as tf
import keras 
from keras.datasets import mnist
import numpy as np
from matplotlib import pyplot as plt 

#load dataset
(train_X, train_y), (test_X, test_y) = mnist.load_data()

#print shapes of vectors? 
print('X_train: ' + str(train_X.shape))
print('Y_train: ' + str(train_y.shape))
print('X_test:  '  + str(test_X.shape))
print('Y_test:  '  + str(test_y.shape))

#plot the dataset 
for i in range(9):  
    plt.subplot(330 + 1 + i)
    plt.imshow(train_X[i], cmap=plt.get_cmap('gray'))
    plt.show()