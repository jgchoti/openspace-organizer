# 2. An openspace

# In `openspace.py` create a class `Openspace` that contains these attributes:

# - `tables` which is a list of `Table`. _(you will need to import `Table` from `table.py`)_. 
# - `number_of_tables` which is an integer.

# And some methods:

# - `organize(names)` that will:
#   - **randomly** assign people to `Seat` objects in the different `Table` objects.
# - `display()` display the different tables and there occupants in a nice and readable way
# - `store(filename)` store the repartition in an excel file
import random
# from .table import Table
class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def __str__(self):
        occupants = ', '.join(f"Seat {i+1}: {seat}" for i, seat in enumerate(self.seats))
        return f"Capacity of {self.capacity} | Occupants: [{occupants}]" 
    
    def assign_seat(self, name: str) -> bool:
        for seat in self.seats:
            if seat.set_occupant(name):
                return True
        return False
class Seat:
    def __init__(self):
        self.free: bool = True
        self.occupant: str = None

    def set_occupant(self, name: str) -> bool:
        if self.free:
            self.occupant = name
            self.free = False
            return True
        return False

    def remove_occupant(self) -> str:
        if not self.free:
            name = self.occupant
            self.occupant = None
            self.free = True
            return name
        return None

    def __str__(self):
        return self.occupant or "Empty"

class Openspace():  
    def __init__(self, number_of_tables: int , table_capacity: int):
        self.number_of_tables = number_of_tables
        self.tables = []
        for item in range(number_of_tables):
            table = Table(capacity=table_capacity)
            self.tables.append(table)
    
# - `organize(names)` that will randomly assign people to `Seat` objects in the different `Table` objects.
    def organize(self, names_list: list[str]):
        random.shuffle(names_list)
        total_seats = sum(table.capacity for table in self.tables)
        seat_index = list(range(total_seats))
        assignments = {}
        all_seats = []
        for table in self.tables:
            all_seats.extend(table.seats)
        for index, name in enumerate(names_list):
            if index < total_seats:
                seat = all_seats[seat_index[index]]
                seat.set_occupant(name)
                assignments[name] = seat
            else:
                assignments[name] = None 
    
        unassigned = [name for name, seat in assignments.items() if seat is None]
        if unassigned:
            print(f"\n⚠️ Couldn't assign these people due to lack of space: {', '.join(unassigned)}")
    
        return assignments


# - `display()` display the different tables and there occupants in a nice and readable way    
    def display(self) -> None:
        print("\n📋 Seating Arrangement:")
        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i}: {table}")        


    
 
                
              
            
        
    



    