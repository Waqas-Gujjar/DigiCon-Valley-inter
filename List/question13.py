# Write a program to remove duplicates from a given list.

list_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 6, 6]
list_without_duplicates = list(set(list_with_duplicates))
print("List without duplicates:", list_without_duplicates)

# output
# List without duplicates: [1, 2, 3, 4, 5, 6]