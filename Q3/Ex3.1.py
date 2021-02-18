hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per Hour:")
r = float(rate)
# Pay the hourly rate for the hours up to 40
#and 1.5 times the hourly rate for all hours worked above 40 hours
if h <= 40:
    gross_pay = h * r
else:
    gross_pay = (40 * r) + (h-40) * r * 1.5

print (gross_pay)
