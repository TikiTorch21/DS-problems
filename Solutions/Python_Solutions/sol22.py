l = [0, 3, 5, 2, 0, 5, 1, 56, 0]


def shift_zero_a1(l):
    """
    Function to shift zeroes
    to beginning of input list.
    (APPROACH 1)

    Parameters
    ----------
    l : list
            input list

    Returns
    -------
    list
            Modified version of input list.
    """
    for idx, n in enumerate(l):
        if n == 0:
            l.pop(idx)
            l.insert(0, 0)
    return l


print(f"Using approach 1:\n\t{shift_zero_a1(l)}")


def shift_zero_a2(l):
    """
    Function to shift zeroes
    to beginning of input list.
    (APPROACH 2)

    Parameters
    ----------
    l : list
            input list

    Returns
    -------
    list
            Sliced version of input list.
    """
    index_ = 0

    for num in l:
        if num == 0:
            continue
        else:
            # Sequentially add non-zero elemts to the list from the beginning

            l[index_] = num
            index_ += 1

    for zero in range(index_, len(l)):
        l[zero] = 0

    return l[index_:] + l[:index_]


print(f"Using approach 2\n\t{shift_zero_a2(l)}")


def shift_zero_a3(l):
    """
    Function to shift zeroes
    to beginning of input list.
    (APPROACH 3)

    Parameters
    ----------
    l : list
            input list

    Returns
    -------
    list
            Modified version of input list.
    """
    s = ""

    for num in l:
        if num == 0:
            s += "0"
    for n_num in l:
        if n_num != 0:
            s += f"{n_num}"

    l = [int(c) for c in s]

    return l


print(f"Using approach 3:\n\t{shift_zero_a3(l)}")


def shift_zero_a4(l):
    """
    Function to shift zeroes
    to beginning of input list.
    (APPROACH 4)

    Parameters
    ----------
    l : list
            input list

    Returns
    -------
    list
            Modified version of input list.
    """
    for _ in range(0, len(l)):
        for idx in range(0, len(l)):
            if l[idx] == 0 and idx != 0 and l[idx - 1] != 0:
                temp = l[idx - 1]
                l[idx - 1] = l[idx]
                l[idx] = temp

    return l


print(f"Using approach 4:\n\t{shift_zero_a4(l)}")

#################################################

"""
Solutions
---------
Using approach 1:
	[0, 0, 0, 3, 5, 2, 5, 1, 56]
Using approach 2
	[0, 0, 0, 3, 5, 2, 5, 1, 56]
Using approach 3:
	[0, 0, 0, 3, 5, 2, 5, 1, 5, 6]
Using approach 4:
	[0, 0, 0, 3, 5, 2, 5, 1, 56]
"""
