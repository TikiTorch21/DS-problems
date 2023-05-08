def bin_conv_a1(d):

	# Using in-built function

	d_abs = abs(d)

	binary = int(bin(d_abs)[2:])

	return binary if d>0 else -binary

print(f"Using approach 1:\n\t{bin_conv_a1(-356)}")


def bin_conv_a2(d):

	# Without using in-built function

	d_temp = abs(d)
	binary = ""

	while d_temp > 0:
		rem = d_temp%2
		binary += str(rem)
		d_temp //=2

	return int(binary) if d>0 else int(binary)*-1

print(f"Using approach 2:\n\t{bin_conv_a2(-356)}")