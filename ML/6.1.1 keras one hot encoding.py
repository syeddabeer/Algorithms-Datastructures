from keras.preprocessing.text import Tokenizer
samples=['the cat sat on the mat.', 'the dog ate my homework.']

# initialize tokenizer
tokenizer = Tokenizer(num_words=1000)
# build the word index on the list of words that we have
tokenizer.fit_on_texts(samples)
word_index = tokenizer.word_index

print("word_index: ", word_index)

sequences = tokenizer.texts_to_sequences(samples)
print("sequences: ", sequences)

one_hot_results = tokenizer.texts_to_matrix(samples, mode='binary')
print("one_hot_results: ", one_hot_results)

print('found %s unique tokens'%len(word_index))








