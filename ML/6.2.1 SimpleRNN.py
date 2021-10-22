# RNN has demerit of vanishing gradient problem
from keras.layers import SimpleRNN
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.preprocessing import sequence
from keras.dataset import imdb
# imdb dataset is retrieved as integers in keras.dataset

max_features = 10000
maxlen = 20
batch_size=32

(input_train, y_train), (input_test, y_test) = imdb.load_data(num_words=max_features)

print(len(input_train), 'train sequences')
print(len(input_test), 'test sequences')

print('pad sequences (samples x time)')
input_train = sequence.pad_sequences(input_train, maxlen=maxlen)
input_test = sequence.pad_sequences(input_test, maxlen=maxlen)

print('input_train shape', input_train.shape)
print('input_test shape', input_test.shape)

from keras.models import Sequential
from keras.models import Dense, Flatten

model = Sequential()
model.add(Embedding(max_features, 32))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history=model.fit(x_train, y_train,
	epochs=10,
	batch_size=,
	validation_split=0.2)


model=Sequential()
model.add(Embedding(10000, 32))
model.add(SimpleRNN(32, return_sequences=True))
model.add(SimpleRNN(32, return_sequences=True))
model.add(SimpleRNN(32, return_sequences=True))
model.add(SimpleRNN(32))
print("model.summary: ", model.summary())