lst = [1, 2, 3, 2]
lst.remove(2)
print(lst)   # [1, 3, 2]
lst.pop()      # removes last
lst.pop(0)     # removes index 0
print(lst)   # [3]
lst.clear()
print(lst)   # []
lst = [10, 20, 30]
print(lst.index(20))  # 1
