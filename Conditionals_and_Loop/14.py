# Write a program to check if a number is an Armstrong number.


num = int(input("Enter a number: "))

temp = num
sum_cubes = 0

while temp != 0:
    digit = temp % 10
    sum_cubes += digit ** len(str(num))
    temp //= 10

if num == sum_cubes:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrongnumber.")


# output
# Enter a number: 6
# 6 is an Armstrong number.

# Enter a number: 133
# 133 is not an Armstrongnumber.
