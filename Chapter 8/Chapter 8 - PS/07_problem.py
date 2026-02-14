def rem(l, word):
    new_list = []
    for item in l:
        if not item == word:
            new_list.append(item)
    return new_list
l = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(rem(l, "cherry"))  