import string
import numpy as np

samples=['the cat sat on the mat.', 'the dog ate my homework.']

characters=string.printable
print(characters)
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

token_index=dict(zip(range(1, len(characters)+1), characters))
print(token_index)

max_length=50

results=np.zeros(shape=
	(len(samples), max_length, max(token_index.keys())+1)
	)

for i, sample in enumerate(samples):
	for j, character in enumerate(sample):
		index = token_index.get(character)
		results[i, j, index] = 1

print("results: ", results)