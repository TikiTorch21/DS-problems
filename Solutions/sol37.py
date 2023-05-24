def valid_ISBN10_a1(ISBN):
    """
    Function to check if ISBN number
    is valid.
    (APPROACH 1)

    Parameters
    ----------
    ISBN : str
        input ISBN number

    Returns
    -------
    bool
        True or False value depending
        on if the input string is a valid ISBN number or not.
    """
    adding = 0
    if len(ISBN) == 10 and ISBN[:9].isdigit():
        for count, digit in enumerate(ISBN, 1):
            if digit == "X":
                adding += 10 * 10
            elif digit.isdigit():
                adding += int(digit) * count
        if adding % 11 == 0:
            return True
    return False


print(f"Using approach 1:\n\t{valid_ISBN10_a1('048665088X')}")


def valid_ISBN10_a2(isbn):
    """
    Function to check if ISBN number
    is valid.
    (APPROACH 2)

    Parameters
    ----------
    ISBN : str
        input ISBN number

    Returns
    -------
    bool
        True or False value depending
        on if the input string is a valid ISBN number or not.
    """
    if len(isbn) == 10:
        value = 0
        for idx, num in enumerate(isbn, start=1):
            try:
                if num == "X" and idx == 10:
                    num = 10

                temp_num = int(num)
                value = value + idx * temp_num

            except ValueError:
                return False

        if value % 11 == 0:
            return True

    return False


print(f"Using approach 2:\n\t{valid_ISBN10_a2('048665088X')}")

##############################################################

"""
Solutions
---------
Using approach 1:
        True
Using approach 2:
        True
"""
