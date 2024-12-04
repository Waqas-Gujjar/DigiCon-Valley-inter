# Write a program to replace all occurrences of a substring in a given string.

string = str(input('Enter a sentance :'))
old_string = str(input('Enter a old_string: '))
new_string = str(input('Enter a new string:'))

result = new_string.replace(old_string,string)

print(f'the modify string is {result}')

# output

# Enter a sentance :hi
# Enter a old_string: how are you
# Enter a new string:i am fine
# the modify string is i am fine