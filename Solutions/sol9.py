def anagrams(word, words):
	return [item for item in words if sorted(item)==sorted(word)]

print(f"Using approach 1:\n\t{anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])}")