report = [
    "Redhead 3",
    "Gadwall 1",
    "Smew 4",
    "Greater-Scaup 10",
    "Redhead 3",
    "Gadwall 9",
    "Greater 15",
    "Common Eider 6",
]


def create_report_a1(report):
    """
    Function to return a list sorted
    by species code and total counts as integers.
    (APPROACH 1)

    Parameters
    ----------
    report : list
        list of common duck names along with counts made by researchers.

    Returns
    -------
    list
        list sorted by species "code"
        and total counts as integers.

    """

    final_data_dict = {}
    report = [item.upper() for item in report]
    for item in report:
        item = item.replace("-", " ")
        item = item.split()

        if len(item[:-1]) == 1:
            if item[0][:6] in final_data_dict:
                final_data_dict[item[0][:6]] += int(item[-1])
            else:
                final_data_dict[item[0][:6]] = int(item[-1])

        elif len(item[:-1]) == 2:
            if f"{item[0][:3]}{item[1][:3]}" in final_data_dict:
                final_data_dict[f"{item[0][:3]}{item[1][:3]}"] += int(item[-1])
            else:
                final_data_dict[f"{item[0][:3]}{item[1][:3]}"] = int(item[-1])

        elif len(item[:-1]) == 3:
            if f"{item[0][:2]}{item[1][:2]}" in final_data_dict:
                final_data_dict[f"{item[0][:2]}{item[1][:2]}"] += int(item[-1])
            else:
                final_data_dict[f"{item[0][:2]}{item[1][:2]}"] = int(item[-1])

        elif len(item[:-1]) == 4:
            if f"{item[0][:1]}{item[1][:1]}" in final_data_dict:
                final_data_dict[f"{item[0][:1]}{item[1][:1]}"] += int(item[-1])
            else:
                final_data_dict[f"{item[0][:2]}{item[1][:1]}"] = int(item[-1])
        elif [item[0], item[1]] == ["LABRADOR", "DUCK"]:
            return "Disqualified data"

    sorted_keys = sorted(list(final_data_dict.keys()))
    final_data = []
    for key in sorted_keys:
        final_data.append(key)
        final_data.append(final_data_dict[key])
    return final_data


print(f"Using approach 1:\n\t{create_report_a1(report)}")


def create_report_a2(names):
    """
    Function to return a list sorted
    by species code and total counts as integers.
    (APPROACH 2)

    Parameters
    ----------
    report : list
    list of common duck names along with counts made by researchers.

    Returns
    -------
    list
    list sorted by species "code"
    and total counts as integers.

    """

    def create_code(name):
        name_list = name.replace("-", " ").split()
        if len(name_list) == 1:
            return name[:6]
        elif len(name_list) == 2:
            return name_list[0][:3] + name_list[1][:3]
        elif len(name_list) == 3:
            return name_list[0][:2] + name_list[1][:2] + name_list[2][:2]
        elif len(name_list) == 4:
            return (
                name_list[0][0] + name_list[1][0] + name_list[2][:2] + name_list[3][:2]
            )

    species = {}
    for name in names:
        name, count = " ".join(name.split()[:-1]), int(name.split()[-1])
        if name == "Labrador Duck":
            return ["Disqualified data"]
        if name not in species:
            species[name] = count
        else:
            species[name] += count

    new_species_list = []
    species_sorted_list = sorted(species)
    for s in species_sorted_list:
        new_species_list.append(create_code(s).upper())
        new_species_list.append(species[s])

    return new_species_list


print(f"Using approach 2:\n\t{create_report_a2(report)}")

###########################################################

"""
Solutions
---------
Using approach 1:
        ['COMEID', 6, 'GADWAL', 10, 'GREATE', 15, 'GRESCA', 10, 'REDHEA', 6, 'SMEW', 4]
Using approach 2:
        ['COMEID', 6, 'GADWAL', 10, 'GREATE', 15, 'GRESCA', 10, 'REDHEA', 6, 'SMEW', 4]
"""
