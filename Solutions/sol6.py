def count_a1(string):
	return {c:string.count(c) for c in string}

print(f"Using approach 1:\n\t{count_a1('')}")

def count_a2(string):
	r = {}

	for c in string:
		if c in r:
			r[c] += 1
		else:
			r[c] = 1
	return r

print(f"Using approach 2:\n\t{count_a2('aabccddd')}")