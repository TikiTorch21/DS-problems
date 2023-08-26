def format_date(date):
    """
    Function to format input string into
    a date.

    Parameters
    ----------
    date : str
            input string

    Returns
    -------
    str
            reformatted version of input string
            MM/DD/YYYY
    """
    spli_dates = date.split("/")
    return f"{spli_dates[2]}{spli_dates[1]}{spli_dates[0]}"


print(f"Using approach 1:\n\t{format_date('01/15/2019')}")

##########################################################

"""
Solutions
---------
Using approach 1:
	20191501
"""
