# While loops are used to repeat a block of code while a condition is true.
# Example 1: A simple while loop that prints numbers from 0 to 4.
i = 1
while i < 6:
    print(i)
    i += 1 # i = i + 1
# Example 2: A while loop that prints the first 10 even numbers.
even_number = 0
while even_number < 20:
    print(even_number)
    even_number += 2
# Example 3: A while loop that calculates the factorial of a number.
number = 5 
factorial = 1
while number > 0:
    factorial *= number
    number -= 1 