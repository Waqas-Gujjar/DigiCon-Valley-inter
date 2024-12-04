# Write a program to split a list into two halves.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

half = len(list1) // 2

first_half = list1[:half]
second_half = list1[half:]


print("First half:", first_half)
print("Second half:",second_half)

# output
# First half: [1, 2, 3, 4, 5]
# Second half: [6, 7, 8, 9, 10]