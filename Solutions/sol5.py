def sum_dig_pow_a1(a, b):
    """
    Function to find numbers in a range
    that fulfills a specific property
    in the problem.

    Parameters
    ----------
    a : int
            Starting number.
    b : int
            Ending number

    Returns
    -------
    list
            List of numbers that fulfill the specific property
            shown in the problem.
    """

    res = []

    for number in range(a, b + 1):
        digits = [int(i) for i in str(number)]
        s = 0

        for idx, val in enumerate(digits):
            s += val ** (idx + 1)

        if s == number:
            res.append(number)
    return res


print(f"Using approach 1:\n\t{sum_dig_pow_a1(1, 10)}")

############################################################

"""
Solutions
---------
Using approach 1:
	[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
