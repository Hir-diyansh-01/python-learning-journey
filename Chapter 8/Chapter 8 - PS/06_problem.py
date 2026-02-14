def inch_to_cms(inches):
    return inches * 2.54
n = int(input("Enter the number of inches: "))
print(f"{n} inches is equal to {inch_to_cms(n)} centimeters.")