# Write a program to remove an element from a dictionary.


dict1 = {"name": "John", "age": 30, "city": "New York"}
dict1.pop("city")

print("Dictionary after removing last item using popitem():",dict1)

# output
# Dictionary after removing last item using popitem(): {'name': 'John', 'age': 30}