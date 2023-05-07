recipe = {
	"flour": 500,
	"sugar": 200,
	"eggs": 1
}

available = {
	"flour": 1200,
	"sugar": 1200,
	"eggs": 5,
	"milk": 200
}

def cakes_a1(recipe, available):
	cakes = {}

	for ingr in recipe:
		if available.get(ingr):
			cakes[ingr] = available[ingr]//recipe[ingr]
		else:
			return 0
	return min(cakes.values())

print(f"Using approach 1:\n\t{cakes_a1(recipe, available)}")

def cakes_a2(recipe, available):
	return min(available.get(k, 0)/recipe[k] for k in recipe)

print(f"Using approach 2: \n\t{cakes_a2(recipe, available)}")