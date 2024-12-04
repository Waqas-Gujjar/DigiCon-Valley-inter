# Write a program to find the maximum of three numbers.

num1 = int(input('Enter a first number: '))
num2 = int(input('Enter a second number: '))
num3 = int(input('Enter a third number: '))

if num1 >= num2 and num1 >= num3:
    maximum = num1
elif num2 >= num1 and num2 >= num3:
    maximum = num2   
else:
    maximum = num3

print(f'the maximum of {num1} , {num2} and {num3} is {maximum}')

# output
# Enter a first number: 5
# Enter a second number: 6
# Enter a third number: 9
# the maximum of 5 , 6 and 9 is 9

