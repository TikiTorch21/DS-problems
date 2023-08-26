def pick_peaks(lis):
    """
    Function to return the positions and the values of the peaks
    of an input array.

    Parameters
    ----------
    lis : list
            input list

    Returns
    -------
    str
            Positions and peaks of input array.
    """
    peaks = []
    pos = []
    a_peak = lis[1]
    idx = 2

    while idx < len(lis) - 1:
        if lis[idx] > a_peak:
            a_peak = lis[idx]
        elif lis[idx] < a_peak:
            peaks.append(a_peak)
            pos.append(idx - 1)
            a_peak = lis[idx + 1]

        idx += 1

    return f"pos: {pos}, peaks: {peaks}"


print(f"Using approach 1:\n\t{pick_peaks([1, 2, 3, 6, 4, 4, 1, 2, 3, 2, 1])}")

##############################################################################

"""
Solutions
---------
Using approach 1:
        pos: [3, 5, 8], peaks: [6, 4, 3]
"""
