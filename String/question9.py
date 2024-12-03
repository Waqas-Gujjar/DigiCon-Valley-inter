# Write a program to count the number of words in a given sentence.

input_sentence = input("Enter a sentence: ")
word_count = len(input_sentence.split())
word_count = 1

for char in input_sentence:
    if char == " ":
     word_count += 1

print("The number of words in the sentence is:",word_count)

# output
# Enter a sentence: what is your name
# The number of words in the sentence is: 4