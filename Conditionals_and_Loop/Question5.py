# Write a program to find the factorial of a given number

number = int(input('Enter a number: '))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f'the factorial of {number} is {factorial}')