# This file is part of the OpenTable project.
# Defining class seats
class Seat:
    def __init__(self):
        self.free = True
        self.occupant = ""

    def set_occupant(self, name):
        if self.free:
            self.occupant = name # allocating the seat to the occupant
            self.free = False
            return True # indicating that the seat was successfully assigned
        else:
            print(f"Seat is already occupied by {self.occupant}.")
        return False

    def remove_occupant(self): # removing the occupant from the seat
        """Remove the occupant from the seat and return their name."""
        if not self.free:
            occupant_name = self.occupant
            self.occupant = ""
            self.free = True
            return occupant_name
        return None
# defining class table
class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)] # creating a list of seats with the given capacity

    def has_free_spot(self):
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.set_occupant(name):
                return True
        return False

    def left_capacity(self):
        return sum(1 for seat in self.seats if seat.free)
