def bin_conv_a1(d):
    """
    Function to convert a
    decimal number to a binary number.
    (APPROACH 1 - using in-built function)

    Parameters
    ----------
    d : int
            Input number

    Returns
    -------
    str
            Binary version of input number.
    """

    d_abs = abs(d)

    binary = int(bin(d_abs)[2:])

    return binary if d > 0 else -binary


print(f"Using approach 1:\n\t{bin_conv_a1(-356)}")


def bin_conv_a2(d):
    """
    Function to convert a
    decimal number to a binary number.
    (APPROACH 2 - manually)

    Parameters
    ----------
    d : int
            Input number

    Returns
    -------
    str
            Binary version of input number.
    """

    d_temp = abs(d)
    binary = ""

    while d_temp > 0:
        rem = d_temp % 2
        binary = str(rem) + binary
        d_temp //= 2

    return int(binary) if d > 0 else int(binary) * -1


print(f"Using approach 2:\n\t{bin_conv_a2(-356)}")

##################################################

"""
Solutions
---------
Using approach 1:
	-101100100
Using approach 2:
	-101100100
"""
