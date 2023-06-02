nums = [2, 4, 6, 8, 10, 3]


def find_outlier_a1(nums):
    """
    Function to find an outlier
    in a list.
    (APPROACH 1)

    Parameters
    ----------
    nums : list
            List of numbers.

    Returns
    -------
    int
            Outlier of the list of numbers.
    """
    par0 = nums[0] % 2

    for x in nums:
        if x % 2 != par0:
            return x


print(f"Using approach 1:\n\t{find_outlier_a1(nums)}")


def find_outlier_a2(nums):
    """
    Function to find an outlier
    in a list.
    (APPROACH 2)

    Parameters
    ----------
    nums : list
            List of numbers.

    Returns
    -------
    int
            Outlier of the list of numbers.
    """
    even_nums = list(filter(lambda x: x % 2 == 0, nums))
    odd_nums = list(filter(lambda x: x % 2 != 0, nums))

    if len(odd_nums) == 1:
        return odd_nums[0]
    return even_nums[0]


print(f"Using approach 2:\n\t{find_outlier_a2(nums)}")
#########################################################################

"""
Solutions
-----------
Using approach 1:
	3
Using approach 2:
	3
"""
