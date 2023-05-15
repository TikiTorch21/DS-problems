def total_overs(bowls):
    """
    Function to take a number of bowls
    and calculate the number of ovals and balls
    bowled.

    Parameters
    ----------
    bowls : int
            number of balls bowled

    Returns
    -------
    float
            the number of ovals and balls in the format
            over.balls
    """
    overs = bowls // 6
    balls = bowls - (overs * 6)

    if balls == 0:
        return overs
    return float(f"{overs}.{balls}")


print(f"Using approach 1:\n\t{total_overs(162)}")

############################################

"""
Solutions
---------
Using approach 1:
	27.2
"""
