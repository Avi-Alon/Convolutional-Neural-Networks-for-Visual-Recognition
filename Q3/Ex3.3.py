#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade according to scale.
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit.
score = input("Enter Score: ")
try:
    f_score = float(score)
except:
    print("Error. can't read this number")
    quit()
if f_score < 0:
    print("Score out of range")
    quit()
elif f_score > 1:
    print("Score out of range")
    quit()
else:
    if f_score >= 0.9:
        print("A")
    elif f_score >= 0.8:
        print("B")
    elif f_score >= 0.7:
        print("C")
    elif f_score >= 0.6:
        print("D")
    else:
        print("F")


