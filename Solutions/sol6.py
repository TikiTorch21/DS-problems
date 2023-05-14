def count_a1(string):
    """
    Function to count all the
    occuring characters in a string.
    (APPROACH 1)

    Parameters
    ----------
    string : str
            Input string.

    Returns
    -------
    dict
            Dictionary w/ the counts of each charcter
            in the format character:count.
    """
    return {c: string.count(c) for c in string}


print(f"Using approach 1:\n\t{count_a1('')}")


def count_a2(string):
    """
    Function to count all the
    occuring characters in a string.
    (APPROACH 2)

    Parameters
    ----------
    string : str
            Input string.

    Returns
    -------
    dict
            Dictionary w/ the counts of each charcter
            in the format character:count.
    """
    r = {}

    for c in string:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    return r


print(f"Using approach 2:\n\t{count_a2('aabccddd')}")

######################################################


"""
Solutions
---------
Using approach 1:
	{}
Using approach 2:
	{'a': 2, 'b': 1, 'c': 2, 'd': 3}
"""
