# List: Ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add an element
fruits.remove("banana")  # Remove an element
print(fruits) 

# Tuple: Ordered, immutable, allows duplicates
colors = ("red", "green", "blue")
print(colors[0])  
print(len(colors))  
# Note: You cannot add or remove elements from a tuple

# Dictionary: Key-value pairs, mutable, unordered 
person = {"name": "Alice", "age": 25, "city": "New York"}
person["age"] = 26  # Update value
person["job"] = "Engineer"  # Add a new key-value pair
del person["city"]  # Delete a key-value pair
print(person)  

