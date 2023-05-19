def ips_between(start, end):
    """
    Function to find the number of IPS
    adresses between input start and input end.

    Parameters
    ----------
    start : str
            input start
    end : str
            input end

    Returns
    -------
    int
            number of IPS adresses between
            input start and input end.
    """
    start = start.split(".")
    end = end.split(".")

    last = int(end[-1]) - int(start[-1])
    slast = (int(end[-2]) - int(start[-2])) * 256
    tlast = (int(end[-3]) - int(start[-3])) * 256 * 256
    first = (int(end[0]) - int(start[0])) * 256 * 256 * 256

    return last + slast + tlast + first


print(
    f"Using approach 1:\n\t{ips_between('10.0.0.0', '10.0.0.50')}, {ips_between('20.0.0.10', '20.0.1.0')}"
)

#############################################################################################################

"""
Solutions
---------
Using approach 1:
	50, 246
"""
