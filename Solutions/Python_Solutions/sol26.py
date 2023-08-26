def iso(s, c):
    """
    Function to determine if two input strings
    are isomorphic.

    Parameters
    ----------
    s : str
            first input string
    c : str
            second input string

    Returns
    -------
    bool
            True or False value depending on
            if two input strings are isomorphic.
    """
    s_dict = {}
    c_dict = {}

    for x in s:
        if x in s_dict.keys():
            s_dict[x] += 1

        else:
            s_dict[x] = 1
    for x in s:
        if x in c_dict.keys():
            c_dict[x] += 1
        else:
            c_dict[x] = 1

    s_list = list(s_dict.values())
    c_list = list(c_dict.values())

    return s_list == c_list


print(f"Using approach 1:\n\t{iso('paper', 'title')}")

######################################################

"""
Solutions
---------
Using approach 1:
	True
"""
