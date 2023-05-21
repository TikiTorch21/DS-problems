import numpy as np


def compute():
    """
    Function to compute the matrix product
    of a 4x2 and 2x4 matrix.

    Parameters
    ----------
    NONE

    Returns
    -------
    numpy array
            product of 4x2 and 2x4 matrix
    """
    m1 = np.array([[1, 4], [2, 5], [4, 2], [6, 8]])
    m2 = np.array([[1, 4, 5, 9], [2, 5, 3, 1]])
    product = np.dot(m1, m2)
    return product


print(f"Using approach 1:\n\t{compute()}")

##########################################

"""
Solutions
---------
Using approach 1:
	[[ 9 24 17 13]
 	[12 33 25 23]
 	[ 8 26 26 38]
 	[22 64 54 62]]
"""
