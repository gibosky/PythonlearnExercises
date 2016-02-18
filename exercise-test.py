hrs = raw_input("Enter Hours:")
2	h = float(hrs)
3	limite = 40
4	rate = 10.5
5	if h > limite :
6	    pay = rate * limite + (rate * 1.5 * (h - limite))
7	else :
8	    pay = rate * h
	print pay