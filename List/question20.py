# Write a program to create a list of squares of the first n natural numbers.


number = int(input('Enter a number: '))

squares_list = [i**2 for i in range(1, number+1)]

print("List of squares:",squares_list)

# output
# Enter a number: 5
# List of squares: [1, 4, 9, 16, 25]