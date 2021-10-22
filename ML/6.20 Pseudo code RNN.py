#Pseudo code RNN

state_t = 0
for input_t in input_sequence:
	output_t = sigmoid(dot(U, input_t) + dot(U, state_t) + b)
	state_t = output_t

# state at t
# iterates over sequence elements
# previous output becomes the state for the next iteration