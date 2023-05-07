nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def phone_num_a1(nums):
	n = ''.join(map(str,nums))
	return f"({n[:3]}) {n[3:6]}-{n[6:]}"

print(f"Using approach 1:\n\t{phone_num_a1(nums)}")

def phone_num_a2(n):
	return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

print(f"Using approach 2: \n\t{phone_num_a2(nums)}")

def phone_num_a3(nums):

	# Using enumerate()

	phone_num = "("

	for idx, num in enumerate(nums):
		phone_num += str(nums[num])

		if idx == 2:
			phone_num += ") "

		if idx == 5: 
			phone_num += "-"

	return phone_num

print(f"Using approach 3:\n\t{phone_num_a2(nums)}")