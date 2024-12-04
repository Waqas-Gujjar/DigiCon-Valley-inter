# Write a program to find the most frequent character in a given string.


original_string = input("Enter a string: ")
char_frquency = {}

for char in original_string:
    if char in char_frquency:
     char_frquency [char]+= 1
    else:
       char_frquency[char]= 1 

result = max(char_frquency,key=char_frquency.get)

print (f'most frequent character:{result}')

# output
# Enter a string: hello would
# most frequent characterl