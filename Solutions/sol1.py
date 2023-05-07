nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def phone_num_a1(nums):

	# Using for loops

	phone_num = "("

	for num in range(3):
		phone_num += str(nums[num])
	phone_num += ") "

	for num in range(4, 7):
		phone_num += str(nums[num])
	phone_num += "-"

	for num in range(7, 10):
		phone_num += str(nums[num])

	return phone_num

print(f"Using approach 1:\n\t{phone_num_a1(nums)}")

def phone_num_a2(nums):

	# Using enumerate()

	phone_num = "("

	for idx, num in enumerate(nums):
		phone_num += str(nums[num])

		if idx == 2:
			phone_num += ") "

		if idx == 5: 
			phone_num += "-"

	return phone_num

print(f"Using approach 2:\n\t{phone_num_a2(nums)}")