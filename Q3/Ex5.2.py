#5.2 Write a program that repeatedly prompts a user for integer numbers
# until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        f_num = float(num)
    except:
        print("Invalid input")
        continue
    if largest is None: # Check if this is the first entered element
        largest = f_num
    elif largest < f_num :
         largest = f_num
    if smallest is None: # Check if this is the first entered element
        smallest = f_num
    elif smallest > f_num :
        smallest = f_num



print("Maximum is", largest)
print("Minimum is" , smallest)