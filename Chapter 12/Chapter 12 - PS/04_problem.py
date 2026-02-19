try:
    a = int(input("Enter a number a: "))
    b = int(input("Enter a number b: "))
    print(a/b)
except ZeroDivisionError as  v:
    print("Infinite")