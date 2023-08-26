def pivot_index_a1(l):
    """
    Function to calculate the pivot index
    of an array.
    (APPROACH 1)

    Parameters
    ----------
    l : list
            input array

    Returns
    -------
    int
            Pivot index
    """
    for n in range(len(l)):
        if sum(l[n + 1 :]) == sum(l[:n]):
            return n
    return -1


print(f"Using approach 1:\n\t{pivot_index_a1([-1, -1, 0, 1, 1, 0])}")


def pivot_index_a2(nums):
    """
    Function to calculate the pivot index
    of an array.
    (APPROACH 2)

    Parameters
    ----------
    l : list
            input array

    Returns
    -------
    int
            Pivot index.
    """
    sumL = 0
    sumR = sum(nums)

    for i in range(len(nums)):
        sumR -= nums[i]

        if sumL == sumR:
            return i
        sumL += nums[i]

    return -1


print(f"Using approach 2:\n\t{pivot_index_a2([-1, -1, -1, -1, -1, -1])}")

#########################################################################

"""
Solutions
---------
Using approach 1:
	5
Using approach 2:
	-1
"""
