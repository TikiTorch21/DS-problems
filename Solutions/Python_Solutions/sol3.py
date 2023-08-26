s = "The-Stealth-Warrior"


def to_camel_case_a1(s):
    """
    Function to convert a string
    to camel case.
    (APPROACH 1)

    Paremeters
    ----------
    s : str
            string input

    Returns
    -------
    str
            Camel-case version of input string
    """
    if s == "":
        return s

    # Replace all delimters by blank space
    s = s.replace("_", "-").replace("-", " ")
    s = s.split()
    new_s = ""

    # The first word would be the same as the input, so ignoring.
    for s_w in s[1:]:
        new_s += s_w[0].upper() + s_w[1:]

    return s[0] + new_s


print(f"Using approach 1:\n\t{to_camel_case_a1(s)}")


def to_camel_case_a2(s):
    """
    Function to convert a string
    to camel case.
    (APPROACH 2)

    Paremeters
    ----------
    s : str
            string input

    Returns
    -------
    str
            Camel-case version of input string
    """
    s = s.replace("_", " ").replace("-", " ")
    s = s.split()

    if len(s) == 0:
        return s
    # using the capitilize funcion in conjunction with join() to make everything into a continous string
    return s[0] + "".join(i.capitalize() for i in s[1:])


print(f"Using approach 2:\n\t{to_camel_case_a2(s)}")

#########################################################################

"""
Solutions
-----------
Using approach 1:
	TheStealthWarrior
Using approach 2:
	TheStealthWarrior
"""
