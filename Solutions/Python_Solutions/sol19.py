def solutions(a, b, c):
    """
    Function to return number of all solutions
    to given equation.

    Parameters
    ----------
    a : int
            first variable of equation
    b : int
            second variable of equation
    c : int
            third variable of equation

    Returns
    -------
    int
            Amount of possibilitest
            to given equation.
    """
    D = b**2 - 4 * a * c
    if D == 0:
        return 1
    else:
        if D < 0:
            return 0
        else:
            return 2


print(f"Using approach 1:\n\t{solutions(1, 0, -1)}")

####################################################

"""
Solutions
---------
Using approach 1:
	2
"""
