# Write a program to find the intersection of two lists.


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection_list = list(set(list1) & set(list2))
print("Intersection of two lists:", intersection_list)

# output
# Intersection of two lists: [4, 5]