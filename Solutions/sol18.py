def perimeter(shape, size):
	def_shape = "s"

	s = int(shape==def_shape)
	c = int(shape!=def_shape)


	p_c, p_s = 2*3.14*size, 4*size

	return c*p_c + s*p_s

print(f"Using approach 1:\n\t{perimeter('s', 7)}, {perimeter('c', 9)}")