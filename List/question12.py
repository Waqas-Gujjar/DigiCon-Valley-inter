# Write a program to find the second largest element in a list.

numbers = [4, 2, 9, 6, 5, 1, 8, 3, 7]
unique_number = sorted(set(numbers),reverse=True)
if len(numbers) < 2:
 print("List must have at least two elements.")
else:
 print("Second largest element:", unique_number[1])

#  output
# second largest element: 8