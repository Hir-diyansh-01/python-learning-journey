'''
a = "a very long string with emails that we want to write to a file"
emails = []
3 seconds later...
'''

f = open("file.txt")
data = f.read()
print(data)
f.close()