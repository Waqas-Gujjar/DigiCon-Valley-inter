# Write a program to update a dictionary with another dictionary.


dict1 = {"name": "John", "age": 30}
dict2 = {"age": 31, "city": "New York"}


dict1.update(dict2)

print("Updated dictionary:",dict1)

# output
# Updated dictionary: {'name': 'John', 'age': 31, 'city': 'New York'}