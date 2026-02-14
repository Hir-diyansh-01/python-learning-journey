import os

# Ask user for directory path
directory_path = input("Enter the directory path: ")

try:
    # Use os.listdir() to list contents
    contents = os.listdir(directory_path)
    
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The directory does not exist.")
except NotADirectoryError:
    print("Error: The path entered is not a directory.")
except PermissionError:
    print("Error: Permission denied to access this directory.")
