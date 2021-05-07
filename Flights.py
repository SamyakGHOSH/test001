class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)

boeing=Flight(4)
people=["Samyak", "Preetansh", "Jia", "Dusky", "Sanskriti"]

for person in people:
    if boeing.add_passenger(person):
        print(f"Ticket for {person} successfully booked")
    else:
        print(f"No space for {person} lol")
