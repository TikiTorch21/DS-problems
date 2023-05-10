def format_date(date):
	spli_dates = date.split("/")
	return f"{spli_dates[2]}{spli_dates[1]}{spli_dates[0]}"

print(f"Using approach 1:\n\t{format_date('01/15/2019')}")