def running_sum(li):
    """
    Function to find and return the running sum
    in an input list of numbers.

    Parameters
    ----------
    li : list
            input list

    Returns
    -------
    list
            running sum in an input list of numbers.
    """
    run_sum = []
    s = 0
    for n in li:
        s += n
        run_sum.append(s)

    return run_sum


print(f"Using approach 1:\n\t{running_sum([1, 1, 1, 1])}, {running_sum([1, 2, 3, 4])}")

#######################################################################################

"""
Solutions
---------
Using approach 1:
	[1, 2, 3, 4], [1, 3, 6, 10]
"""
