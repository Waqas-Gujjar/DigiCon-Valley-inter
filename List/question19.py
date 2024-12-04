# Write a program to rotate a list by a given number of positions.

list1 = [1, 2, 3, 4, 5]
positions = 2

rotated_list = list1[positions:] + list1[:positions]

print("Rotated list:",rotated_list)

# output
# Rotated list: [3, 4, 5, 1, 2]
