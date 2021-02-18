#4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay should be the normal rate for hours up to 40
# and time-and-a-half for the hourly rate for all hours worked above 40 hours.
#Put the logic to do the computation of pay in a function called computepay()
# and use the function to do the computation.

def computepay(h,r):
# Pay the hourly rate for the hours up to 40
# and 1.5 times the hourly rate for all hours worked above 40 hours
    if h <= 40:
        gross_pay = h * r
    else:
        gross_pay = (40 * r) + (h - 40) * r * 1.5
    return gross_pay

hrs = input("Enter Hours:")
f_hrs = float(hrs)
rate = input("Enter Rate per Hour:")
f_rate = float(rate)
#Calling a function to compute the gross pay
p = computepay(f_hrs,f_rate)
print("Pay",p)