p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your message: ")

if(p1 in message):
    print("This is a spam message.")
elif(p2 in message):
    print("This is a spam message.")
elif(p3 in message):
    print("This is a spam message.")
elif(p4 in message):
    print("This is a spam message.")
else:
    print("This is not a spam message.")