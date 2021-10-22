from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import os

maxlen=100
training_samples = 200
validation_samples = 10000
max_words = 10000

tokenizer=Tokenizer(num_words=max_words)
# texts is obtained after obtaining the text from previous file handline script
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

word_index=tokenizer.word_index
print('found %s unique tokens'% len(word_index))
#texts_to_matrix

data=pad_sequences(sequences, maxlen=maxlen)

labels=np.array(labels)
print('shape of data tensor: ', data.shape)
print('shape of label tensor: ', label.shape)

indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]

x_train = data[:training_samples]
y_train = labels[:training_samples]
x_val = data[training_samples:training_samples+validation_samples]
y_val = labels[training_samples:training_samples+validation_samples]

