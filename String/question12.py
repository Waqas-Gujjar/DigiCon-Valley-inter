# Write a program to find the first occurrence of a substring in a given string.


string = 'Hello,World!,World Cup'
substring = str(input('Enter a substring: '))

index = string.find(substring)

if index != -1:
    print(f'This string index are found {index}')
else:
    print(f'this string are not found {index}')

    # output
# Enter a substring: hello
# this string are not found -1    

# Enter a substring: World
# This string index are found 6