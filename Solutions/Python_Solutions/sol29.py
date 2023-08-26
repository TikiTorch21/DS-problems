def harshad(num):
    """
    Function to check if input integer
    is a harshad number.

    Parameters
    ----------
    num : int
            input num

    Returns
    -------
    bool
            True or False value depending on
            if input num in a harshad number.
    """
    s_num = str(num)
    temp = 0

    for n in s_num:
        temp += int(n)

    return num % temp == 0


print(f"Using approach 1:\n\t{harshad(18)}")

############################################

"""
Solutions
---------
Using approach 1:
	True
"""
