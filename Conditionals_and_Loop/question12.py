# Write a program to reverse a given number.

num = int(input("Enter a number: "))
reverse_of_number = 0


while num != 0:
    digit = num % 10
    reverse_of_number = reverse_of_number * 10 + digit
    num //= 10


print(f"The sum of the digits is {reverse_of_number}")

# output
# Enter a number: 30
# The sum of the digits is 3