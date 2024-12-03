# Write a program to calculate the Body Mass Index (BMI) given height and weight

height = int(input("Enter A height: "))
weight = int(input("Enter a weigth : "))

mass = (weight / height) * 2 * 703

print(f'the mass of body index {mass}')

# output
# Enter A height20
# Enter a weigth : 30
# the mass of body index 2109.0