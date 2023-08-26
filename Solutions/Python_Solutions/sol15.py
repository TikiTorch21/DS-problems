def check_palin_a1(s):
    """
    Function to check if input string
    (excluding puncuation or special chars)
    is a palindrome.
    (APPROACH 1 - Non-recursive)

    Parameters
    ----------
    s : str
            input string

    Returns
    -------
    str
            "palindrome" if input string is a palindome
            and "not palindrome" if input string is not a palindrome.
    """
    punc = [",", ".", "!", "?", ";", ":", " "]
    new_s = "".join([i for i in s if i not in punc])

    if new_s == new_s[::-1]:
        return "palindrome"

    return "not palindrome"


print(f"Using approach 1:\n\t{check_palin_a1('attpptta')}")


def check_palin_a2(s):
    """
    Function to check if input string
    (excluding puncuation or special chars)
    is a palindrome.
    (APPROACH 2 - Recursive)

    Parameters
    ----------
    s : str
            input string

    Returns
    -------
    str
            "palindrome" if input string is a palindome
            and "not palindrome" if input string is not a palindrome.
    """
    punc = [",", ".", "!", "?", ";", ":", " "]
    new_s = "".join([i for i in s if i not in punc])

    if len(s) < 2:
        return "palindrome"
    if new_s[0] != new_s[-1]:
        return "not palindrome"

    return check_palin_a2(s[1:-1])


print(f"Using approach 2:\n\t{check_palin_a2('attpptta')}")

###########################################################

"""
Solutions
---------
Using approach 1:
	palindrome
Using approach 2:
	palindrome
"""
