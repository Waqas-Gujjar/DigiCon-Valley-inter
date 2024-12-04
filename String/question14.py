# Write a program to split a string based on a delimiter.



string = str(input('Enter a sentance :'))
print(string)

delimiter = str(input('Enter a delimiter: '))
split_list = string.split(delimiter)

print(f"The split list is {split_list}")


# output
# Enter a sentance :hello
# hello
# Enter a delimiter: hello
# The split list is ['', '']
