sen = "The-Stealth-Warrior"

def to_camel_case_a1(sen):
	if "_" in sen:
		split_sen = sen.split("_")
	else:
		split_sen = sen.split("-")

	camel_sen = ""

	camel_sen += split_sen[0]

	for word_num in range(1, len(split_sen)):
		if split_sen[word_num][0].islower():
			camel_sen += split_sen[word_num][0].upper()
			camel_sen += split_sen[word_num][1:len(split_sen[word_num])]
		else:
			camel_sen += split_sen[word_num]

	return camel_sen



print(f"Using approach 1:\n\t{to_camel_case_a1(sen)}")