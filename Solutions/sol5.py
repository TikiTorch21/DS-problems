def sum_dig_pow(a, b):
	res = []

	for number in range(a, b+1):
		digits = [int(i) for i in str(number)]
		s = 0

		for idx, val in enumerate(digits):
			s += val ** (idx+1)

		if s == number:
			res.append(number)
	return res

print(f"Using approach 1:\n\t{sum_dig_pow(1, 10)}")