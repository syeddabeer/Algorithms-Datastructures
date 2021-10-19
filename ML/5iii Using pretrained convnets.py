

# using pretrained convnets
# feature extraction
# pretrained network = base model -> local highly generic feature maps
# new classifier = head model -> not generic
# pretrained models - keras.applications module

from keras.applications import VGG16
base_model = VGG16(weights='imagenet', include_top=False, 
					input_shape=(150,150,3))
#input_shape is optional

import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

base_dir='/users/Downloads/cats_dogs_images'
train_dir=os.path.join(base_dir,'train')
test_dir=os.path.join(base_dir,'test')
validation_dir=os.path.join(base_dir,'validation')

datagen=ImageDataGenerator(rescale=1./255)
batch_size=20

def extract_features(directory, sample_count):
	features=np.zeros(shape=(sample_count, 4, 4, 512))
	labels=np.zeros(shape=(sample_count)
	generator=datagen.flow_from_directory(
		directory,
		target_size=(150,150),
		batch_size=batch_size,
		class_mode='binary')
	i=0
	for input_batch, labels_batch in generator:
		features_batch = base_model.predict(inputs_batch)
		features[i*batch_size : (i+1) * batch_size]=features_batch
		labels[i*batch_size : (i+1) * batch_size]=labels_batch
		i+=1
		for i*batch_size>=sample_count:
			break
	return features, labels

train_features, train_labels = extract_features(train_dir, 2000)
validation_features, validation_labels = extract_features(validation_dir, 2000)
test_features, test_labels = extract_features(test_dir, 2000)

train_features=np.reshape(train_features, (2000, 4 * 4 * 512))
validation_features=np.reshape(validation_features, (1000, 4 * 4 * 512))
test_features=np.reshape(test_features, (1000, 4 * 4 * 512))


# head classifier
from keras import models
from keras import layers
from keras import optimizers

model = models.Sequential()
model.add(layers.Dense(256, activation='relu', input_dim=4 * 4 * 512))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))

#fine tuning
model.compile(optimizer=optimizers.RMSprop(lr=2e-5),
	loss='binary_crossentropy',
	metrics=['acc'])

history=model.fit(train_features, train_labels, epochs=30, batch_size=20,
	validation_data=(validation_features, validation_labels))




# using freezing

model = models.Sequential()
model.add(base_model)
base_model.trainable=False
model.add(layers.Dense(256, activation='relu', input_dim=4 * 4 * 512))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))