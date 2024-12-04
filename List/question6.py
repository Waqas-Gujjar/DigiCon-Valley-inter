# Write a program to remove all occurrences of a given element from a list.


number = int(input('Enter a number: '))
lists = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]



for i in range(lists.count(number)):
    lists.remove(number)

print(lists)    

# output
# Enter a number: 2
# [1, 3, 6, 3, 8, 9, 7, 3]


