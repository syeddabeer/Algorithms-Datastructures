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