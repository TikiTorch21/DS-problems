def total_overs(bowls):
	overs = (bowls//6)
	balls = bowls - (over*6)

	if balls == 0:
		return overs
	return float(f"{overs}.{balls}")

print(f"Using approach 1:\n\t{total_overs}")