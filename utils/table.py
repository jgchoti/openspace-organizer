class Seat:
    def __init__(self):
        self.free = True
        self.occupant = ""

    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False
            return True
        return False

    def remove_occupant(self):
        if not self.free:
            occupant_name = self.occupant
            self.occupant = ""
            self.free = True
            return occupant_name
        return None
    def __str__(self):
        return self.occupant or "Empty"

class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self):
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.set_occupant(name):
                return True
        return False

    def left_capacity(self):
        return sum(1 for seat in self.seats if seat.free)
    
    def __str__(self):
        occupants = ', '.join(f"Seat {i+1}: {seat}" for i, seat in enumerate(self.seats))
        return f"Capacity of {self.capacity} | Occupants: [{occupants}]" 
    
