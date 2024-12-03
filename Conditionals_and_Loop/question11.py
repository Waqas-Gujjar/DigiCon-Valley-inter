# Write a program to find the sum of the digits of a given number.

num = int(input("Enter a number: "))
sum_of_digits = 0


while num != 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10


print(f"The sum of the digits is {sum_of_digits}")

# output
# Enter a number: 20
# The sum of the digits is: 2
