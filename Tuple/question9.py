# Write a program to check if an element exists in a tuple.

tuple1 = (1, 2, 3, 4, 5)

element = int(input('Enter a number : '))

if element in tuple1:
 print(element, "exists in the tuple.")
else:
 print(element, "does not exist in the tuple.")

#  output
# Enter a number : 2
# 2 exists in the tuple.