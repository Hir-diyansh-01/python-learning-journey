# Using the walrus operator (:=) in Python
# The walrus operator assigns values to variables as part of an expression

# Example 1: Basic usage in a while loop
numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(f"Processing {n} numbers")
    numbers.pop()

# Example 2: Using in list comprehension
data = [1, 2, 3, 4, 5]
squared = [x**2 for x in data if (doubled := x * 2) > 4]
print(squared)