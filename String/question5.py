# Write a program to count the number of vowels in a given string.


input_string = str(input('Enter a vowelword: '))
vowel_count  = 0
vowel_words = 'aeiouAEIOU'

for char in input_string:
    if char in vowel_words:
        vowel_count += 1

print("The number of vowels in the string is:",vowel_count)