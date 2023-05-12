def ips_between(start, end):
	start = start.split(".")
	end = end.split(".")

	last = int(end[-1])-int(start[-1])
	slast = (int(end[-2]) - int(start[-2]))*256
	tlast = (int(end[-3]) - int(start[-3]))*256*256
	first = (int(end[0]) - int(start[0])) *256*256*256

	return last+slast+tlast+first

print(f"Using approach 1:\n\t{ips_between('10.0.0.0', '10.0.0.50')}")