# Write a program to calculate compound interest.


principal_amount = float(input('Enter a valu of Principal: '))
interest_rate = float(input('Enter a value of rate: '))
number_of_years = int(input("Enter the number of years: "))

compound_interest = principal_amount * (1 + interest_rate/100) ** number_of_years - principal_amount

print("Compound Interest: ", compound_interest)

# output
# Enter a valu of Principal: 20
# Enter a value of rate: 30
# Enter the number of years: 2
# Compound Interest:  13.800000000000004