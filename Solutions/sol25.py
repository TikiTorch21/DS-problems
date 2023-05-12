def pivot_index_a1(l):
	for n in range(len(l)):
		if sum(l[n+1:]) == sum(l[:n]):
			return n
	return -1

print(f"Using approach 1:\n\t{pivot_index_a1([-1, -1, 0, 1, 1, 0])}")

def pivot_index_a2(nums):
	sumL = 0
	sumR = sum(nums)

	for i in range(len(nums)):
		sumR -= nums[i]

		if sumL == sumR:
			return i
		sumL += nums[i]

	return -1

print(f"Using approach 2:\n\t{pivot_index_a2([-1, -1, -1, -1, -1, -1])}")