d = {"z": "q", "w": "f"}


def invert(d):
    """
    Function to invert keys of input dictionary.

    Parameters
    ----------
    d : dict
            input dictionary

    Returns
    -------
    dict
            inverted version of input dictionary.
    """
    return {v: k for k, v in d.items()}


print(f"Using approach 1:\n\t{invert(d)}")

##########################################

"""
Solutions
---------
Using approach 1:
	{'q': 'z', 'f': 'w'}
"""
