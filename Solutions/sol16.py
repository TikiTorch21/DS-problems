def operation(operation, inp1, inp2=None):
    """
    Function to perform one operation:
            1) Sum of digits in a number
            2) Find a raised to the power b
            3) Reverse a string

    Parameters
    ----------
    operation : int
            operation type
    """

    def sum_digits(n):
        if n < 10:
            return n

        return n % 10 + sum_digits(n // 10)

    def power(num, exp):
        if exp == 1:
            return num
        return num * power(num, exp - 1)

    def reverse_rec(s):
        if len(s) == 1:
            return s

        return reverse_rec(s[1:]) + s[0]

    if operation == 1:
        return sum_digits(inp1)
    elif operation == 2:
        return power(inp1, inp2)
    elif operation == 3:
        return reverse_rec(inp1)


print(f"Using approach 1:\n\t{operation(2, 4, 3)}")

###################################################

"""
Solutions
---------
Using approach 1:
	64
"""
