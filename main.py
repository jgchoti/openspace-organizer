import os
from utils.openspace import Openspace
from utils.config import CSV_FILE_PATH

def main() -> None:
    # - load the colleagues from the csv file defined in the config file
    path = os.path.abspath("")
    access_file = os.path.join(path, CSV_FILE_PATH )
    names_list =[]

    try:
        with open(access_file, "r", encoding='latin-1') as source_file:
            for line in source_file:
                name = line.strip()
                names_list.append(name)
    except:
        raise ValueError("Unsupported file format. Use .csv")
    
    user_name = input("Please enter your name : ")
    if user_name in names_list:
        print(f"Hi, {user_name}! Your name is already on the list.")
    else:
        names_list.append(user_name)
        print(f"Welcome {user_name}, your name has been added to the list.")
    
    number_participant = len(names_list)
    print("🚀🪑 Launching Openspace Organizer... ")
    print("👋🏽 Welcome!", names_list)
    print(f"🤹 There are {number_participant} people. Let's get organize (randomly)")
    # - Launch the organizer. Display the results  
    openspace = Openspace(number_of_tables=6, table_capacity=4)
    # Organize seating
    openspace.organize(names_list)
    # Display seating
    openspace.display()
    
if __name__ == "__main__":
    main()



   


