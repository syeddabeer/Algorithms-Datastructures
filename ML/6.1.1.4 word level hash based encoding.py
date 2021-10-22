#6.1.1
# word level encoding

import numpy as np

samples = ['the cat sat on the mat.', 'the dog ate my homework.']

#token_index={}
# for sample in samples:
# 	for word in sample.split():
# 		if word not in token_index:
# 			token_index[word] = len(token_index)+1
# print(token_index)

dimensionality = 1000
max_length = 10

print(len(samples))
# print(max(token_index.values()))

results = np.zeros(shape=(len(samples), max_length, dimensionality
	))
print(results)
for i, sample in enumerate(samples):
	for j, word in list(enumerate(sample.split()))[:max_length]:
		print("j: ", j, "word: ", word)
		index = abs(hash(word))
		print("index: ")
		results[i,j,index]=1
print(results)

# IndexError: index 4601330597061722551 is out of bounds for axis 2 with size 1000
# [Finished in 271ms]