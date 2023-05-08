def hex_conv_a1(d):

	# Using in-built function

	if d>=0:
		return hex(d)[2:]
	else:
		return "-"+hex(d)[3:]

print(f"Using approach 1:\n\t{hex_conv_a1(5600)}")

def hex_conv_a2(x):

	# Without using in-built function

	keys = list(range(16))
	values = list(map(str, range(10))) + ["A", "B", "C", "D", "E", "F"]
	hex_table = dict(zip(keys, values))

	d = x*-1 if x<0 else x

	hex_d = ""
	while d>0:
		rem = d%16

		hex_d = hex_table[rem] + hex_d
		d //=16

	if x<0:
		return "-"+hex_d

	return hex_d

print(f"Using approach 2:\n\t{hex_conv_a2(-5600)}")