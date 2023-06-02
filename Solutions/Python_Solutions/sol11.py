import math


def line_length(x1, y1, x2, y2):
    """
    Function that takes two coordinates of two points
    and returns length of line segment connecting two points.

    Parameters
    ----------
    x1 : int
            x coordinate of the first set
    y1 : int
            y coordinate of the first set
    x2 : int
            x coordinate of the second set
    y2 : int
            y coordinate of the second set

    Returns
    -------
    float
            length of line segment connecting
            the two input points (x1, y1), (x2, y2).
    """
    ll = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(ll, 2)


print(f"Using approach 1:\n\t{line_length(0, 0, 1, 1)}")

########################################################

"""
Solutions
---------
Using approach 1:
	1.41
"""
