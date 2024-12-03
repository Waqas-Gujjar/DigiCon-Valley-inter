# Write a program to check if a number is a palindrome.

input_string = str(input('Enter a sentance: '))
palindrom = input_string.replace(' ','').lower()

if input_string == palindrom :
    print("palindrom string")
else:
    print('Not a palindrome string') 

    # output  
    
# Enter a sentance: waqasgujjar
# palindrom string

# Enter a sentance: waqas gujjar
# Not a palindrome string