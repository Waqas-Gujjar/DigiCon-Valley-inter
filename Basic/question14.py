# Write a program to convert days into weeks and years.

day = int(input('Enter a day: '))

week = day / 7

year = 365 / week

print(f"day = {day}")
print(f"week = {week}")
print(f"year = {year}")

# output
# Enter a day: 2
# day = 2
# week = 0.2857142857142857
# year = 1277.5
