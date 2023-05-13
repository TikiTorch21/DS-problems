import numpy as np

def identity_a1():

	# Using .identity

	identity = np.identity(3, dtype="int")

	return identity

print(f"Using approach 1:\n\t{identity_a1()}")

def identity_a2():

	# Using .eye
	
	return np.eye(3, dtype="int")

print(f"Using approach 2:\n\t{identity_a2()}")

def identity_a3():

	# Manually

	m = np.zeros((3, 3), dtype="int")

	for row in range(3):
		for column in range(3):
			if row == column:
				m[row, column] = 1
	return m

print(f"Using approach 3:\n\t{identity_a3()}")