def pick_peaks(lis):
	peaks = []
	pos = []
	a_peak = lis[1]
	idx = 2

	while idx < len(lis)-1:
		if lis[idx]>a_peak:
			a_peak = lis[idx]
		elif lis[idx]<a_peak:
			peaks.append(a_peak)
			pos.append(idx-1)
			a_peak = lis[idx+1]

		idx += 1

	return f"pos: {pos}, peaks: {peaks}"

print(f"Using approach 1:\n\t{pick_peaks([1, 2, 3, 6, 4, 4, 1, 2, 3, 2, 1])}")