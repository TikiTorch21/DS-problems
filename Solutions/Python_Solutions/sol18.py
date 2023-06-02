def perimeter(shape, size):
    """
    Function to find and return perimeter
    of either a square or a circle.
    CAN ONLY USE ARITHMETIC/COMPARISON OPERATIORS
            - No if..else statements
            - No dictionaries
            - No formatting methods

    Parameters
    ----------
    shape : str
            Shape that code finds the perimeter of
            s for square and c for circle

    size : int
            size of the input shape, depending on which shape.
            For example, the size of the square would be the sides,
            but for the circle it would be the diameter.

    Returns
    -------
    int
            Perimeter of input shape(square or circle)
    """
    def_shape = "s"

    s = int(shape == def_shape)
    c = int(shape != def_shape)

    p_c, p_s = 2 * 3.14 * size, 4 * size

    return c * p_c + s * p_s


print(f"Using approach 1:\n\t{perimeter('s', 7)}, {perimeter('c', 9)}")

#######################################################################

"""
Solutions
---------
Using approach 1:
	28.0, 56.52
"""
