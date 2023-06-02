import numpy as np


def identity_a1():
    """
    Function to create an identity matrix
    of order 3.
    (APPROACH 1 - Using .identity)

    Parameters
    ----------
    NONE

    Returns
    -------
    numpy array
            idendity matrix of order 3
    """

    identity = np.identity(3, dtype="int")

    return identity


print(f"Using approach 1:\n\t{identity_a1()}")


def identity_a2():
    """
    Function to create an identity matrix
    of order 3.
    (APPROACH 2 - Using .eye)

    Parameters
    ----------
    NONE

    Returns
    -------
    numpy array
            idendity matrix of order 3
    """

    return np.eye(3, dtype="int")


print(f"Using approach 2:\n\t{identity_a2()}")


def identity_a3():
    """
    Function to create an identity matrix
    of order 3.
    (APPROACH 3 - Manual approach)

    Parameters
    ----------
    NONE

    Returns
    -------
    numpy array
            idendity matrix of order 3
    """

    m = np.zeros((3, 3), dtype="int")

    for row in range(3):
        for column in range(3):
            if row == column:
                m[row, column] = 1
    return m


print(f"Using approach 3:\n\t{identity_a3()}")

##############################################

"""
Solutions
---------
Using approach 1:
	[[1 0 0]
 	[0 1 0]
 	[0 0 1]]
Using approach 2:
	[[1 0 0]
 	[0 1 0]
 	[0 0 1]]
Using approach 3:
	[[1 0 0]
 	[0 1 0]
 	[0 0 1]]
"""
