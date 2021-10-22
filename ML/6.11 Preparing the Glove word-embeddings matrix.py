from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import os
# import optimizers

imdb_dir = '/Uses/dsyed/Downloads/ac1Imdb'
train_dir = os.path.join(imdb_dir, 'train')

labels=[]
texts=[]

for label_type in ['neg', 'pos']:
	dir_name = os.path.join(train_dir, label_type)
	for fname in os.listdir(dir_name):
		if fname[-4:] == '.txt':
			f = open(os.path.join(dir_name, fname))
			texts.append(f.read())
			f.close()

			if label_type == 'neg':
				labels.append(0)

			else:
				labels.append(1)

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

#6.10 parsing the glove embedding file

glove_dir = '/Users/dsyed/Downloads/glove.6B'
# url to download https://nlp.stanford.edu/projects/glove/

f = open(os.path.join(glove_dir, 'glove.6B.100d.txt'))

for line in f:
	values = line.split()
	word = values[0]
	coefs = np.asarray(values[1:], dtype='float32')
	embeddings_index[word]=coefs

f.close()

print('Found %s word vectors'% len(embeddings_index))

# This returns embeddings_index with word and coefs forward. variable is embeddings_index


#6.11 Preparing the Glove word-embeddings matrix

embedding_dim = 100

embedding_matrix = np.zeros((max_words, embedding_dim))

for word, i in word_index.items():
	if i < max_words:
		embedding_vector = embeddings_index.get(word)
		if embedding_vector is not None:
			embedding_matrix[i] = embedding_vector


from keras.models import Sequential, Flatten, Dense, Embedding
model=Sequential()
model.add(Embedding(max_words, embedding_dim, input_length=maxlen))
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()

model.layers[0].set_weights([embedding_matrix])
model.layers[0].trainable = False

# words not found in the embedding index will be all zeros.

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
history=model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_val,y_val))

model.save_weights('pre_trained_glove_model.h5')


# Tokenizing the data of the dataset
test_dir = os.path.join(imdb_dir, 'test')
labels = []
texts =[]
for label_type in ['neg', 'pos']:
	dir_name = os.path.join(test_dir, label_type)
	for fname in sorted(os.listdir(dir_name)):
		if fname[-4:] == '.txt':
			f = open(os.path.join(dir_name, fname))
			texts.append(f.read())
			f.close()

			if label_type == 'neg':
				labels.append(0)
			else:
				labels.append(1)

sequences=tokenizer.texts_to_sequences(texts)
x_test = pad_sequences(sequences, maxlen = maxlen)
y_test = np.asarray(labels)



