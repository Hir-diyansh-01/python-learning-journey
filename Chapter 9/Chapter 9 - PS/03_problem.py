import os

def generateTable(n):
    base_path = os.path.dirname(__file__)   # current file ka folder
    folder_path = os.path.join(base_path, "tables")

    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, f"table_{n}.txt")

    with open(file_path, "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n*i}\n")

for i in range(2, 21):
    generateTable(i)
