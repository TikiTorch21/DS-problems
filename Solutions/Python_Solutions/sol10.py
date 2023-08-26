def number_length_a1(num):
    """
    Function that takes a number as input
    and returns number of digits in the number.
    (APPROACH 1)

    Parameters
    ----------
    num : int
            input number

    Returns
    -------
    int
            number of digits in input num.
    """
    num = abs(num)
    d = 0

    if num < 10:
        return d + 1

    while num > 0:
        # Keep removing digits one by one and increment d

        num //= 10
        d += 1
    return d


print(f"Using approach 1:\n\t{number_length_a1(-23001)}")


def number_length_a2(num):
    """
    Function that takes a number as input
    and returns number of digits in the number.
    (APPROACH 2)

    Parameters
    ----------
    num : int
            input number

    Returns
    -------
    int
            number of digits in input num.
    """
    count = 0

    if num <= 9:
        return count + 1
    if num < 0:
        while num != 0:
            count += 1
            num //= -10

    while num != 0:
        count += 1
        num //= 10
    return count


print(f"Using approach 2:\n\t{number_length_a2(20)}")

#####################################################

"""
Solutions
---------
Using approach 1:
	5
Using approach 2:
	2
"""
