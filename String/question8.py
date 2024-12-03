# Write a program to reverse a given string.

input_string = input("Enter a string: ")


reversed_string = input_string[::-1]


reversed_string = "".join(reversed(input_string))

print("The reversed string is:", reversed_string)

# output

# Enter a string: hello
# The reversed string is: olleh