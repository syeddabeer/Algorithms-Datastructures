from keras.preprocessing.image import ImageDataGenerator

# data augmentation
# for more options, check keras documentation
datagen=ImageDataGenerator(
	rescale=1./255,
	rotation_range=40,      #rotation shift : 0-180
	width_shift_range=0.2,
	height_shift_range=0.2,
	shear_range=0.2,    #random shearing transformation
	zoom_range=0.2,
	horizontal_flip=True,
	fill_mode='nearest'   #filling newly generated pixels
	)
test_datagen  = ImageDataGenerator(rescale=1./255)

#reads images from the directory
train_generator = train_datagen.flow_from_directory(
	train_dir,
	target_size=(150,150),
	batch_size=20,
	class_mode='binary')

test_generator = test_datagen.flow_from_directory(
	validation_dir,
	target_size=(150,150),
	batch_size=20,
	class_mode='binary')

#binary_crossentropy loss requires binary labels

for data_batch, labels_batch in train_generator:
	print("data_batch.shape: ", data_batch.shape)
	break


history = model.fit_generator(
	train_generator,
	steps_per_epoch=100,
	epochs=30,
	validation_data=validation_generator,
	validation_steps=50
	)


model.save('cats_and_dogs.h5')

import matplotlib.pyplot as plt

acc=history.history['acc']
val_acc=history.history['val_acc']
loss=history.history['loss']
val_loss=history.history['val_loss']

epochs=range(1, len(acc)+1)
plt.plot(epochs, acc, 'bo', label='Training_acc')
plt.plot(epochs, val_acc, 'bo', label='val_acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training_loss')
plt.plot(epochs, val_loss, 'bo', label='val_loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()


