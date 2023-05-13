def harshad(num):
	s_num = str(num)
	temp = 0

	for n in s_num:
		temp += int(n)

	return num % temp == 0

print(f"Using approach 1:\n\t{harshad(18)}")