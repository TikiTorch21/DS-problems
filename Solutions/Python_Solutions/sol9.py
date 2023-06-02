def anagrams(word, words):
    """
    Function to find anagram of input word
    in list of words.

    Parameters
    ----------
    word : str
            input word.
    words : list
            list of words

    Returns:
    list
            List of items in the input list
            that are anagrams of input word.
    """
    return [item for item in words if sorted(item) == sorted(word)]


print(
    f"Using approach 1:\n\t{anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])}"
)

##################################################################################################

"""
Solutions
---------
Using approach 1:
	['carer', 'racer']
"""
