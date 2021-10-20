print(model.summary())
base_model.trainable=True

trainable_Flag=False

for layer in base_model.layers:
	if layer.name == 'block5_conv1':
		trainable_Flag = True 
	if trainable_Flag:
		layer.trainable = True
	else:
		layer.trainable = False 


model.compile(loss='binary_crossentropy',
	optimizer=optimizers.RMSprop(lr=1e-5),
	metrics=['acc'])

history= model.fit_generator(
	train_generator,
	steps_per_epoch=100,
	epochs=100,
	validation_data=validation_generator,
	validation_steps=50)