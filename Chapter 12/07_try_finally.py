def main():
    try:
        a = int(input("Enter a number: "))
        print(f"You entered: {a}")
        return 

    except Exception as e:
        print(f"An error occurred: {e}")
        return

    finally:
        print("No exceptions were raised. The input was successful.")


main()