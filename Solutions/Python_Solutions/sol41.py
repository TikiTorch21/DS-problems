from itertools import product


def get_pins_a1(observed):
    """
    Function to find all the alternate combinations
    of an input code.

    Parameters
    ----------
    observed : str
        input code.

    Returns
    -------
    list
        list of alternate combinations from the input code.

    """
    possiblities = {
        "1": ["1", "2", "4"],
        "2": ["1", "2", "3", "5"],
        "3": ["2", "3", "6"],
        "4": ["1", "4", "5", "7"],
        "5": ["2", "4", "5", "6", "8"],
        "6": [],
    }

    if len(observed) == 1:
        return possiblities[observed]
    else:
        output = list()
        all_combs_list = [possiblities[digit] for digit in observed]
        for ele in product(*all_combs_list):
            output.append("".join(map(str, ele)))

    return output


print(get_pins_a1("1"))


def get_pins_a2(observed):
    adj = {
        "1": "124",
        "2": "2135",
        "3": "326",
        "4": "4157",
        "5": "52468",
        "6": "6359",
        "7": "748",
        "8": "85790",
        "9": "968",
        "0": "08",
    }

    result = [""]
    for d in observed:
        result = [prefix + c for prefix in result for c in adj[d]]
    return result


print(get_pins_a2("1"))

"""
Solutions
---------
Using approach 1: 
    ['1', '2', '4']
Using approach 2: 
    ['1', '2', '4']
"""
