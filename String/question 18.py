# Write a program to find the frequency of each character in a given string.



original_string = input("Enter a string: ")
char_frquency = {}

for char in original_string:
    if char in char_frquency:
     char_frquency [char]+= 1
    else:
       char_frquency[char]= 1 

print (char_frquency)

# output
# Enter a string: hello
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

