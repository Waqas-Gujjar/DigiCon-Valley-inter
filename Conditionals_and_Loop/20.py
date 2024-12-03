# Write a program to count the number of digits in a given number.

num = int(input("Enter a number: "))

count = 0
while num != 0:
    num //= 10
    count += 1

print("The number of digits is:",count)

# output
# Enter a number: 10000
# The number of digits is: 5
