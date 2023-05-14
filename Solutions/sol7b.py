def hex_conv_a1(d):
    """
    Function to convert a
    decimal number to a
    hexadecimal number.
    (APPROACH 1 - using in-built function)

    Parameters
    ----------
    d : int
            Input number

    Returns
    -------
    str
            Hexadecimal version of input number.
    """

    if d >= 0:
        return hex(d)[2:]
    else:
        return "-" + hex(d)[3:]


print(f"Using approach 1:\n\t{hex_conv_a1(5600)}")


def hex_conv_a2(x):
    """
    Function to convert a
    decimal number to a
    hexadecimal number.
    (APPROACH 2 - manually)

    Parameters
    ----------
    x : int
            Input number

    Returns
    -------
    str
            Hexadecimal version of input number.
    """

    keys = list(range(16))
    values = list(map(str, range(10))) + ["A", "B", "C", "D", "E", "F"]
    hex_table = dict(zip(keys, values))

    d = x * -1 if x < 0 else x

    hex_d = ""
    while d > 0:
        rem = d % 16

        hex_d = hex_table[rem] + hex_d
        d //= 16

    if x < 0:
        return "-" + hex_d

    return hex_d


print(f"Using approach 2:\n\t{hex_conv_a2(-5600)}")

###################################################

"""
Solutions
---------
Using approach 1:
	15e0
Using approach 2:
	-15E0
"""
