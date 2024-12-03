# Write a program to print the first n odd numbers.

number = int(input("Enter a number: "))


for i in range(1, 2 * number ,2):
    print(i)
   
print("The first", number, "odd numbers are")

# output
# Enter a number: 8
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# The first 8 odd numbers are