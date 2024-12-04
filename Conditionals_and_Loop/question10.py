# Write a program to find the greatest common divisor (GCD) of two numbers.

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

GDC = 1

for i in range(1,min(number1,number2)):
    if number1 % i == 0 or number2 % i == 0:
        GDC = i

print(f'GDC of {number1} and {number2} = {GDC}')

# output
# Enter a number: 30
# Enter a number: 60
# GDC of 30 and 60 = 20