def check_fib_count(n):
    """

    Function to calculate the nth element in the Fibonacci sequence,
    and then count the occurence of each digit in the number.

    Parameters
    ----------
    n : int
        index of the fibonacci number you want to find.

    Returns
    -------
    list
        A list of tuples that contains the information
        of the occurence of each digit in the number.

    """

    def fib_rec_mem(n, fib_dict):
        if n not in fib_dict:
            fib_dict[n] = fib_rec_mem(n - 1, fib_dict) + fib_rec_mem(n - 2, fib_dict)

        return fib_dict[n]

    f_number = fib_rec_mem(n, {1: 0, 2: 1})

    count_list = []
    s_fnumber = str(f_number)

    for digit in s_fnumber:
        count = 0
        for check_digit in s_fnumber:
            if digit == check_digit:
                count += 1
        count_list.append((int(digit), count))
        s_fnumber = s_fnumber.replace(digit, "")

    for t in count_list:
        if 0 in t:
            count_list.pop(count_list.index(t))
    return f"In {f_number}, the occurences are {count_list}"


print(f"Using approach 1\n\t{check_fib_count(15)}")

####################################################

"""
Solutions
---------
Using approach 1
        In 377, the occurences are [(3, 1), (7, 2)]
"""
