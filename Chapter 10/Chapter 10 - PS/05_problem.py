from random import randint

class Train: 

    def __init__(self, train_number):
        self.train_number = train_number

    def book(self, from_station, to_station):
        print(f"Ticket is booked in train number {self.train_number} from {from_station} to {to_station}")

    def getStatus(self):
        print(f"Status of train number {self.train_number} is: On Time")

    def getFare(self,from_station, to_station):
        print(f"Fare for train number {self.train_number} from {from_station} to {to_station} is: {randint(100, 500)}")

t = Train(12345)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")