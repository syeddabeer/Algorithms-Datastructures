from keras import layers
from keras import models

model = models.Sequential()

#adding the layers
#MNIST image format - 28 * 28 * 1
# common choice of filter or kernel is 3 by 3
model.add(layers.Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(28, 28, 1)))
# shape becomes n-f+1, n-f+1, input_depth
model.add(layers.MaxPooling2D(pool_size=(2,2)))
# shape becomes n/2, n/2, d
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3,3), activation='relu'))

print(model.summary())
"""
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 26, 26, 32)        320       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 13, 13, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 11, 11, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 5, 5, 64)          0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 3, 3, 64)          36928     
=================================================================
Total params: 55,744
Trainable params: 55,744
Non-trainable params: 0
_________________________________________________________________
"""

# add a classifier on top of the convnet
model.add(layers.Flatten())                      # 3d to 1d conversion
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))


print(model.summary())
"""
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 26, 26, 32)        320       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 13, 13, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 11, 11, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 5, 5, 64)          0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 3, 3, 64)          36928     
_________________________________________________________________
flatten_1 (Flatten)          (None, 576)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 64)                36928     
_________________________________________________________________
dense_2 (Dense)              (None, 10)                650       
=================================================================
Total params: 93,322
Trainable params: 93,322
Non-trainable params: 0
_________________________________________________________________
"""


from keras.datasets import mnist
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# data normalization
train_images=train_images.reshape((60000, 28, 28, 1))
train_images=train_images.astype('float32')/255
test_images=test_images.reshape((10000, 28, 28, 1))
test_images=test_images.astype('float32')/255

# get dummies for the labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# compile function
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# fit function
model.fit(train_images, train_labels, epochs=5, batch_size=64)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print(test_acc)