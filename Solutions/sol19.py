def solutions(a, b, c):
	D = b**2 - 4*a*c
	if D == 0:
		return 1
	else:
		if D<0:
			return 0
		else:
			return 2

print(f"Using approach 1:\n\t{solutions(1, 0, -1)}")