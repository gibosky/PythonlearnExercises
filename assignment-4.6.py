def computepay(h, r):
    limite = 40
    if h > limite :
        pay = r * limite + (r * 1.5 * (h - limite))
    else:
        pay = r * h
    return pay

hrs_input = raw_input("Enter Hours:")
rate_input = raw_input("Enter Rate:")
hrs = float(hrs_input)
rate = float(rate_input)
p = computepay(hrs, rate)
print p