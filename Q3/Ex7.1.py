#7.1 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
# printing the file, line by line
for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
# saving the file as a string and then, printing the file as one long string
#fh_as_string = fh.read()
#fh_upper = fh_as_string.upper()
#print (fh_upper.rstrip())
##### I have added the following lines beyond the requirements of this exercise #####
# string_to_look_for = "AND"
# x = fh_upper.count(string_to_look_for)
# print("\nThe word", string_to_look_for, "apears ", x , "times in the text")