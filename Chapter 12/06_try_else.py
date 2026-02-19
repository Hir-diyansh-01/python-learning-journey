try:
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")

except Exception as e:
    print(f"An error occurred: {e}")

else:
    print("No exceptions were raised. The input was successful.")   