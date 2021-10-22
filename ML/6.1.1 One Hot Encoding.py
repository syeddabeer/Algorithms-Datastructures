#6.1.1
# word level encoding

import numpy as np

samples = ['the cat sat on the mat.', 'the dog ate my homework.']

token_index={}

for sample in samples:
	for word in sample.split():
		if word not in token_index:
			token_index[word] = len(token_index)+1

print(token_index)
max_length = 10

print(len(samples))
print(max(token_index.values()))

results = np.zeros(shape=(len(samples), max_length, max(token_index.values()) + 1
	))
print(results)
for i, sample in enumerate(samples):
	for j, word in list(enumerate(sample.split()))[:max_length]:
		print("j: ", j, "word: ", word)
		index = token_index[word]
		results[i,j,index]=1
print(results)