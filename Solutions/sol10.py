def number_length_a1(num):

	# Version 1 more optimized

	num = abs(num)
	d = 0

	if num<10:
		return d+1

	while num>0:
		#Keep removing digits one by one and increment d

		num //=10
		d+=1
	return d


print(f"Using approach 1:\n\t{number_length_a1(-23001)}")

def number_length_a2(num):

	# Version 2 needs to be more optimized

	count = 0

	if num<=9:
		return count+1
	if num<0:
		while num!=0:
			count+=1
			num //=-10

	while num!=0:
		count +=1
		num //= 10
	return count
print(f"Using approach 2:\n\t{number_length_a2(20)}")








