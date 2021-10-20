from keras.models import load_model

model=load_model('cats_dogs.h5')
print(model.summary())

img_path='/Users/dsyed/cat1.jpg'

from keras.preprocessing import image
import numpy as np

img=image.load_img(img_path, target_size=(150, 150,))

img_tensor=image.img_to_array(img)
img_tensor=np.expand_dims(img_tensor, axis=0)
img_tensor /= 255.

# showing the image
import matplotlib.pyplot as plt
plt.imshow(img_tensor[0])
plt.show()

# extracting the outputs of the model intermediate layers
from keras import models
layer_outputs = [layer_output for layer in model.layers[:8]]
activation_model = models.Model(inputs=model.input, outputs=layer_outputs)

activations = activation_model.predict(img_tensor)