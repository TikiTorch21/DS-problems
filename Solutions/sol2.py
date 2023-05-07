nums = [2, 4, 6, 8, 10, 3]

def outlier_a1(nums):
	even_nums = []
	odd_nums = []

	for number in nums:
		if number % 2 == 0:
			even_nums.append(number)
		else:
			odd_nums.append(number)

	if len(odd_nums) == 1:
		return odd_nums[0]
	return even_nums[0]

print(f"Using approach 1:\n\t{outlier_a1(nums)}")

def outlier_a2(nums):
	even_nums = list(filter(lambda x: x%2 == 0, nums))
	odd_nums = list(filter(lambda x: x%2 != 0, nums))

	if len(odd_nums) == 1:
		return odd_nums[0]
	return even_nums[0]

print(f"Using approach 2:\n\t{outlier_a2(nums)}")