# Write a program to find the sum of n natural numbers.

number = int(input('Enter a number: '))

if number < 0:
    print('Enter a positive number')
else :
    sum = 0
    while number > 0:
        sum += number
        number -= 1

    print(f'the sum of number {sum}')
    # output

# Enter a number: 16
# the sum of number 136
  
     

