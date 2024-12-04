# Write a program to print the Fibonacci sequence up to a given number.

number = int(input('Enter a number: '))
n1,n2 = 0,1
count = 0

if number <= 0 :
    print('Please enter a positive number')
elif number == 1 :
    print('Fibonacci sequence is',number,':')
    print(n1)
else:
    while count < number :
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1

# output
# Enter a number: 20
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377
# 610
# 987
# 1597
# 2584
# 4181

  