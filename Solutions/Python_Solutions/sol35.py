def give_change_a1(money):
    """
    Function to break money down to
    smallest number of bills possible.
    (APPROACH 1 - USING DICTIONARY)

    Parameters
    ----------
    money : int
        amount of money given.

    Returns
    -------
    tuple
        Tuple of the bills the money
        was broken down into.

    """

    bills_dict = {1: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}

    for bill in [100, 50, 20, 10, 5, 1]:
        bills_dict[bill] = money // bill
        money -= bill * (money // bill)

    return tuple(bills_dict.values())


print(f"Using approach 1:\n\t{give_change_a1(217)}")


def give_change_a2(amount):
    """
    Function to break money down to
    smallest number of bills possible.
    (APPROACH 2 - Using variables)

    Parameters
    ----------
    money : int
        amount of money given.

    Returns
    -------
    tuple
        Tuple of the bills the money
        was broken down into.

    """
    hundredd = amount // 100
    fiftyd = (amount - 100 * hundredd) // 50
    twentyd = (amount - 100 * hundredd - 50 * fiftyd) // 20
    tend = (amount - 100 * hundredd - 50 * fiftyd - 20 * twentyd) // 10
    fived = (amount - 100 * hundredd - 50 * fiftyd - 20 * twentyd - 10 * tend) // 5
    oned = (
        amount - 100 * hundredd - 50 * fiftyd - 20 * twentyd - 10 * tend - 5 * fived
    ) // 1

    return (oned, fived, tend, twentyd, fiftyd, hundredd)


print(f"Using approach 2:\n\t{give_change_a2(217)}")

#####################################################

"""
Solutions
---------
Using approach 1:
        (2, 1, 1, 0, 0, 2)
Using approach 2:
        (2, 1, 1, 0, 0, 2)
"""
