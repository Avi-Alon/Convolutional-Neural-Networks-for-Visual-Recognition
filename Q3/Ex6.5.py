#6.5 Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
colon_pos = text.find(":") #finding colon position
num_with_whitespace = text[colon_pos + 1 :] #slicing all the text after the colon
clean_num = num_with_whitespace.lstrip()
f_clean_num = float(clean_num)
print(clean_num)