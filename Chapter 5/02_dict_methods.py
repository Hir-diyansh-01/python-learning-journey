marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
# Accessing values
# print(marks.items())  # dict_items([('Alice', 85), ('Bob', 92), ('Charlie', 78)])
# print(marks.keys())   # dict_keys(['Alice', 'Bob', 'Charlie'])
# print(marks.values()) # dict_values([85, 92, 78])
# Updating values
# marks["Alice"] = 90
# print(marks)  # {'Alice': 90, 'Bob': 92,
 

# Adding new key-value pair
# marks["David"] = 88
# print(marks)  # {'Alice': 90, 'Bob': 92, 'Charlie': 78, 'David': 88}

print(marks.get("Alice"))  # 90
print(marks["Alice"])  # 90