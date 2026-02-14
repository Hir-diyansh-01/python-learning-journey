def multiply(n):
    for i in range(1, 11):
        print(f"{i} x {n} = {i*n}")
number = int(input("Enter a number: "))
multiply(number)