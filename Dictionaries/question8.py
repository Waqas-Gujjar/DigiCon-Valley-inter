# Write a program to merge two dictionaries.


dict1 = {"name": "John", "age": 30}
dict2 = {"city": "New York", "country": "USA"}

merged_dict = {**dict1, **dict2}

print("Merged dictionary:", merged_dict)

# output
# Merged dictionary: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
