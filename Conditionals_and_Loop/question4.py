# Write a program to check if a year is a leap year.

year = int(input("Enter a year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))


elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))


else:
    print("{0} is not a leap year".format(year))

# output

# Enter a year: 2000
# 2000 is a leap year