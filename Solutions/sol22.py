def shift_zero_a1(l):
	for idx, n in enumerate(l):
		if n==0:
			l.pop(idx)
			l.insert(0, 0)
	return l

print(f"Using approach 1:\n\t{shift_zero_a1([0, 3, 5, 2, 0, 5, 1, 56, 0])}")

def shift_zero_a2(l):
	index_ = 0

	for num in l:
		if num == 0:
			continue
		else:
			# Sequentially add non-zero elemts to the list from the beginning

			l[index_] = num
			index_ += 1

	for zero in range(index_, len(l)):
		l[zero] = 0

	return l[index_:] + l[:index_]

print(f"Using approach 2\n\t{shift_zero_a2([0, 3, 5, 2, 0, 5, 1, 56, 0])}")