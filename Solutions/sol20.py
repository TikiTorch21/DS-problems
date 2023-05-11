d = {"z": "q", "w": "f"}

def invert(d):
	return {v: k for k, v in d.items()}

print(f"Using approach 1:\n\t{invert(d)}")