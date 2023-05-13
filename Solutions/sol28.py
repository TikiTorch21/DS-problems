import numpy as np

def compute():
	m1 = np.array([[1,4], [2,5], [4,2], [6,8]])
	m2 = np.array([[1,4,5,9],[2,5,3,1]])
	product = np.dot(m1, m2)
	return product

print(f"Using approach 1:\n\t{compute()}")