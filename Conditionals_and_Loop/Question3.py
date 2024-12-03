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

