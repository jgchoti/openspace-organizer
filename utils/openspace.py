import random
import os
import csv
from .table import Table
class Openspace():  
    def __init__(self, number_of_tables: int , table_capacity: int):
        self.number_of_tables = number_of_tables
        self.tables = []
        for item in range(number_of_tables):
            table = Table(capacity=table_capacity)
            self.tables.append(table)
    
# - `organize(names)` that will randomly assign people to `Seat` objects in the different `Table` objects.
    def organize(self, names_list: list[str]):
        random.shuffle(names_list) # Shuffle people
        total_seats = self.tables[0].capacity * self.number_of_tables 
        
        all_seats = []
        for table in self.tables:
            all_seats.extend(table.seats) # single list of every seat from all tables.
        random.shuffle(all_seats) # Shuffle seats
        
         # Clear seats before assignment
        for seat in all_seats:
            seat.remove_occupant()
        
        unassigned = []
        for index, name in enumerate(names_list):
            if index < total_seats:
                seat = all_seats[index]
                seat.set_occupant(name) # Assign the person to this seat
            else:
                unassigned.append(name) # If no seats are left, add the person to the unassigned list
    
        if unassigned:
            print(f"\n⚠️ Couldn't assign these people due to lack of space: {', '.join(unassigned)}")
            user_prompt = input("Do you want to add another table? (yes/no): ").lower().strip()
            if user_prompt in ("yes", "y"):
                self.add_table(4)
                print("➕ Added new table. Reorganizing seats...🔃")
                self.organize(names_list)  # call to reorganize with new table(s)
            else:
                print(f"🚫 No additional table added. {', '.join(unassigned)} remain unassigned. 😥")
            

# Add Table
    def add_table(self, table_capacity: int):
        self.tables.append(Table(table_capacity))
        self.number_of_tables += 1


# - `display()` display the different tables and there occupants in a nice and readable way    
    def display(self) -> None:
        print("\n📋 Seating Arrangement:")
        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i}: {table}")        
            
#store file
    def storefile(self):
        #user input file name 
        filename = input("Enter the filename to save seating arrangement or 'q' if you don't want to save the file: ").strip()
        if filename.lower() == 'q':
            print("No file saved!")
            return
        if not filename:
            filename = "seating_plan"    
        if not filename.endswith('.csv'):
            filename += '.csv'
        # save to directory
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Table Number", "Seat Number", "Occupant"])
            for table_idx, table in enumerate(self.tables, start=1):
                for seat_idx, seat in enumerate(table.seats, start=1):
                    occupant = seat.occupant or "Empty"
                    writer.writerow([table_idx, seat_idx, occupant])
        
        print(f"Seating arrangement saved to {filename}")
    

    
 
                
              
            
        
    



    