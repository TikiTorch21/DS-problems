def solution(lis):

	# Variables
	pos = 1
	visited = [lis[0]]
	jumps = 1

	# Condition
	out = False

	while out == False:
		if pos >= len(lis):
			return jumps
		visited.append(lis[pos])
		pos += lis[pos]
		jumps += 1

print(f"Using approach 1:\n\t{solution([1, 2, 2, 9, 1, 1, 1, 1, 1, 1, 1, 2, -1])}")