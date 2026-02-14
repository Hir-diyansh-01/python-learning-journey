marks1 = int(input("Enter the marks of first subject: "))
marks2 = int(input("Enter the marks of second subject: "))
marks3 = int(input("Enter the marks of third subject: "))

total_percentage =(100*(marks1 + marks2 + marks3) / 300) 

if(total_percentage >= 40):
    if(marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
        print("You are passed!")
    else:
        print("You are failed because you have less than 33% in one or more subjects.")
else:
    print("You are failed because your total percentage is less than 40%.")