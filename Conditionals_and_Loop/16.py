# Write a program to find the sum of squares of n natural numbers.

number = int(input('Enter a number: '))
sum_of_squares = 0



for i in range(1,number+1):
    sum_of_squares += i ** 2

print (f'the sum of squres {number} and natural number { sum_of_squares}')  

# output
# Enter a number: 10
# the sum of squres 10 and natural number 385
    

