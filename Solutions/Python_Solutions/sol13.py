def top_note_a1(info):
    """
    Function to take an input dict of grades
    and return the top grade.
    (APPROACH 1)

    Parameters
    ----------
    info : dict
            input dict

    Returns
    -------
    dict
            modified version of input dictionary.
    """
    info["top_notes"] = max(info["notes"])
    info.pop("notes")
    return info


print(f"Using approach 1:\n\t{top_note_a1({'name': 'Zygmund', 'notes': [1, 2, 3] })}")


def top_note_a2(info):
    """
    Function to take an input dict of grades
    and return the top grade.
    (APPROACH 2)

    Parameters
    ----------
    info : dict
            input dict

    Returns
    -------
    dict
            dictionary of name and top grade.
    """
    output = {}
    output["name"] = info["name"]
    output["top_notes"] = max(info["notes"])

    return output


print(f"Using approach 2:\n\t{top_note_a2({'name': 'Zygmund', 'notes': [1, 2, 3] })}")
######################################################################################

"""
Solution
--------
Using approach 1:
	{'name': 'Zygmund', 'top_notes': 3}
Using approach 2:
	{'name': 'Zygmund', 'top_notes': 3}
"""
