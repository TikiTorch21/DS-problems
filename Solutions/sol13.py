def top_note_a1(info):
	info["top_notes"] = max(info["notes"])
	info.pop("notes")
	return info

print(f"Using approach 1:\n\t{top_note_a1({'name': 'Zygmund', 'notes': [1, 2, 3] })}")



def top_note_a2(info):

	output = {}
	output["name"] = info["name"]
	output["top_notes"] = max(info["notes"])

	return output

print(f"Using approach 2:\n\t{top_note_a2({'name': 'Zygmund', 'notes': [1, 2, 3] })}")