from keras.layers import Embedding

embedding_layer = Embedding(1000, 64)
# 1000 - 1+ max word index
# dimensionality here is 64