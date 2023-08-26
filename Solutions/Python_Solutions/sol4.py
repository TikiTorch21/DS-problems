recipe = {"flour": 500, "sugar": 200, "eggs": 1}

available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}


def cakes_a1(recipe, available):
    """
    Function to find number of cakes
    that could be baked.
    (APPROACH 1)

    Parameters
    ----------
    recipe : dict
            recipe to bake a cake
    available : dict
            ingredients that are available

    Returns
    -------
    int
            Number of cakes that could be baked
            based on what's available.
    """
    cakes = {}

    for ingr in recipe:
        if available.get(ingr):
            cakes[ingr] = available[ingr] // recipe[ingr]
        else:
            return 0
    return min(cakes.values())


print(f"Using approach 1:\n\t{cakes_a1(recipe, available)}")


def cakes_a2(recipe, available):
    """
    Function to find number of cakes
    that could be baked.
    (APPROACH 2)

    Parameters
    ----------
    recipe : dict
            recipe to bake a cake
    available : dict
            ingredients that are available

    Returns
    -------
    int
            Number of cakes that could be baked
            based on what's available.
    """
    return int(min(available.get(k, 0) / recipe[k] for k in recipe))


print(f"Using approach 2: \n\t{cakes_a2(recipe, available)}")


################################################################

"""
Solutions
----------
Using approach 1:
	2
Using approach 2: 
	2
"""
