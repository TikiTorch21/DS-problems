import math

def line_length(x1, y1, x2, y2):
	ll = math.sqrt((x2-x1)**2(y2-y1)**2)
	return round(ll, 2)

print(f"Using approach 1:\n\t{line_length(0, 0, 1, 1)}")