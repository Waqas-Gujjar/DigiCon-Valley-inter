# Write a program to remove all spaces from a string.

original_string = input("Enter a string: ")

string_without_spaces = original_string.replace(" ", "")

print("Original String: ", original_string)
print("String after removing all spaces: ", string_without_spaces)

# output
# Enter a string: hello world
# Original String:  hello world
# String after removing all spaces:  helloworld