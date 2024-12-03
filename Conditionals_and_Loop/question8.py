# Write a program to print all prime numbers between two given numbers.


number = int(input('Enter a number: '))
var = False
if number == 0 or number == 1 :
    print(f'{number} is not a prime number')
elif number > 1:
    for i in range (2,number):
        if (number % 2 ) == 0 :

            var = True
            break
if var:
    print(f'{number} is not a prime number')       
else:
    print(f'{number} is a prime number')       