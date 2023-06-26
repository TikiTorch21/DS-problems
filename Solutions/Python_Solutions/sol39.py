import statistics
from statistics import mode


def zero_or_one(n, array):
    """
    Function to take two parameters:
    n and array, and return a list of length n.
    List contains number with max amount of occurences
    for each column.
    
    Parameters
    ----------
    n : int
        number of sublists in array.
    array : list
        input array.

    Returns
    -------
    list
        list of length n, with the list containing number with
        max amount of occurences for each column.
    """
    temp_array = []
    if n == 1:
        return array[0]

    for ele_idx in range(0, n + (len(array[0]) - n)):
        temp = []
        for lis_idx in range(0, n):
            temp.append(array[lis_idx][ele_idx])
        temp_array.append(temp)

    return [mode(lis) for lis in temp_array]


print(
    f"Using approach 1(Three test cases):\n\t{zero_or_one(1, [[1,1,0,1]])}, {zero_or_one(3, [[1,0,1,0,1], [1,0,1,0,1], [0,1,0,1,0]])}, {zero_or_one(5,  [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]])}"
)

"""
Using approach 2
"""

zero_or_one_w_lambda = lambda n, s: [max(c, key=c.count) for c in zip(*s)]

s = [
    [1, 0, 0, 0, 2],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 4],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]

print(
    f"Using approach 2(Three test cases):\n\t{zero_or_one_w_lambda(1, [[1,1,0,1]])}, {zero_or_one_w_lambda(3, [[1,0,1,0,1], [1,0,1,0,1], [0,1,0,1,0]])}, {zero_or_one_w_lambda(5,  [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]])}"
)
###############################################################################################################################################################################################################################

"""
Solutions
---------
Using approach 1(Three test cases):
        [1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 0, 0, 0, 0]
Using approach 2(Three test cases):
        [1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 0, 0, 0, 0]
"""
