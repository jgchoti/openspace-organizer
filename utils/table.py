#  A table

# We define a table with how many seats it encompasses and we define the object in the `table.py` file

# ##### 1.1 Seat

# In `table.py`:

# Create a class called `Seat` with two attributes:
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
# - `free` which is a boolean.
# - `occupant` which is a string.

# and 2 functions : 

# - `set_occupant(name)` which allows the program to assign someone a seat if it's free
# - `remove_occupant()` which  remove someone from a seat and return the name of the person occupying the seat before

# ##### 1.2 Table

# In the same file, create a class `Table` with ? attributes:

# - `capacity` which is an integer
# - `seats` which is a list of `Seat` objects (size = `capacity`)

# and 3 functions : 
# - `has_free_spot()` that returns a boolean (True if a spot is available)
# - `assign_seat(name)` that places someone at the table
# - `left_capacity()` that returns an integer
