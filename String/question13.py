# Write a program to find the last occurrence of a substring in a given string.



string = 'Hello,World!,World Cup'
substring = str(input('Enter a substring: '))

index = string.rfind(substring)

if index != -1:
    print(f"The last occurrence of the substring is at index {index}")
else:
    print(f'this string are not found {index}')

    # output
# Enter a substring: hello
# this string are not found -1    

# Enter a substring: World Cup
# The last occurrence of the substring is at index 13