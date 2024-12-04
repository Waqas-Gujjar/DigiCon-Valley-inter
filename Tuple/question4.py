# Write a program to find the index of an element in a tuple.

number= int(input('Enter a number: '))
tuple1 = (1, 2, 3,100,11,145,124,1,12,14,16,)

tuple_index = tuple1.index(number)
print(f'the index of tuple is: {tuple_index}')

# output
# the index of tuple is: 10