l = ["A", "A", "A", "B", "B", "C", "A"]


def getWinner_a1(l):
    """
    Function to find the winner
    from an input list of ballots.
    (APPROACH 1)

    Parameters
    ----------
    l : list
            input list

    Returns
    -------
    str
            election winner.
    """
    d = dict()
    length = len(l) // 2

    for name in l:
        if name in d.keys():
            d[name] += 1
        else:
            d[name] = 1

    greatest = 0
    winner = list(filter(lambda x: d[x] > length, d.keys()))

    if len(winner) == 0:
        return "No Winner"

    return winner[0]


print(f"Using approach 1:\n\t{getWinner_a1(l)}")


def getWinner_a2(ballots):
    """
    Function to find the winner
    from an input list of ballots.
    (APPROACH 2)

    Parameters
    ----------
    l : list
            input list

    Returns
    -------
    str
            election winner.
    """
    candidates = {candidate: ballots.count(candidate) for candidate in set(ballots)}

    for candidate in candidates:
        if candidates[candidate] > len(ballots) / 2:
            return candidate


print(f"Using approach 2:\n\t{getWinner_a2(l)}")

################################################

"""
Solutions
---------
Using approach 1:
        A
Using approach 2:
        A
"""
