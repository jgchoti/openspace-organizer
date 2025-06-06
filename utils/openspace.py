import random
# from .table import Table

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


    
 
                
              
            
        
    



    