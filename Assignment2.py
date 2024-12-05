"""
File Name: hotel_management.py
Author: Khoa Hoa Giang Nguyen
Description: A simple hotel management system that handles room reservations, billing, and room details.
Date: 2024-12-02
"""
import os
import datetime
from datetime import datetime
# Define the name of the room allocation file and backup file with timestamp
roomfile = "LHMS_850001676.txt"
backupfile = "LHMS_850001676_backup{}.txt".format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))


# Function to Save room allocation to a file
def save_room_allocation_to_file():
    try:
        with open(roomfile, "w") as file:  # Open the file specified by 'roomfile' in write mode
            for roomnumber, details in rooms.items():  # Iterate through all rooms and their details
                # Format room details as a string
                rooms_detail = f"Room Number : {roomnumber}, Type: {details['RoomType']}, Price: {details['Price']}, Reserved: {details['allocated']}\n"
                file.write(rooms_detail)# Write the formatted string to the file
        print(f"Room allocation has been saved to {roomfile}")  # Notify the user that the data has been successfully saved
    except IOError as e:
        # Catch and print any I/O errors
        print(f"Error saving to file {roomfile}: {e}")


# Function to read and display room allocation details from a file


def show_room_allocation_from_a_file():
    try:
        # Check if the room allocation file exists
        if os.path.exists(roomfile):
            # Open the file in read mode
            with open(roomfile, "r") as file:
                # Read the entire content of the file
                content = file.read()
                # Check if the file has content
                if content:
                    # If content is present, print it to the console
                    print("Room allocation from file:\n")
                    print(content)
                else:
                    # If the file is empty, inform the user
                    print("No room allocation data found in file")
        else:
            # If the file does not exist, inform the user
            print(f"{roomfile} does not exist !!!")
    except Exception as e:
        # Catch and print any errors that occur during the file operation
        print(f"Error reading from allocation: {e}")
# Backup room allocation file


def backup_room_allocation():
    try:
        if os.path.exists(roomfile): # Check if the original room allocation file exists
            with open(roomfile,"r") as original_file: # Open the original room allocation file in read mode
                content = original_file.read() # Read the content of the original file

            with open(backupfile, "w") as backup:# Create a backup file and write the content to it
                backup.write(content)

            # Deleting content in the original file
            with open(roomfile, "w") as file:
                file.truncate(0)# This removes all the content from the file

            print(f"Backup created as {backupfile} and the orginal file {roomfile} have been cleared.")
        else:
            print(f"{roomfile} doesn't exist !!!")# If the original file doesn't exist, print an error message
    except Exception as e:
        print(f"An Erro occur during backup operation: {e}") # Handle and print any errors that occur during the backup process

# Room List and reservation status
# Assume this is basic price, incase customer want to check room's price
rooms = {
    101: {"RoomType": "Single", "Price": 100, "allocated": False},
    102: {"RoomType": "Double", "Price": 150, "allocated": False},
    103: {"RoomType": "Suite", "Price": 250, "allocated": False},
}
# AddRoom
"""
   Add a new room to the system.
   Prompts the user for room number, type, and price.
   Updates the rooms dictionary with the new room details.
   """


def addroom():
    try:
        Roomnumber = int(input("Enter Room number: "))  # Take the room number
        RoomType = input("Enter type of room(Single, Double, Suite): ")  # Take room Type
        RoomPrice = int(input("Set the room's price: "))  # Take room price
        if RoomPrice <= 0: # Ensure the hotel income :D:D
            print("Are you working for free ?? enter a number greater than zero")
            return
        rooms[Roomnumber] = {"RoomType": RoomType, "Price": RoomPrice, "allocated": False}  # Add the room to the dictionary
        print(f'Room {Roomnumber} has been added to the system !!!')
    except ValueError:
        print("Invalid input. Please ensure you enter valid data for room number and price.")


# Delete room
"""
    Delete a room from the system based on the room number input by the user.
    Checks if the room exists in the system and deletes it if found.
    """


def delete_room():
    try:
        Roomnumber = int(input("Enter room number to delete: ")) #Take the room number want to delete
        if Roomnumber not in rooms:# If the room does not exist, inform the user and return
            print("Room not found !!!")
            return
        del rooms[Roomnumber] #Delete the room from the dictionary
        print(f"Room number {Roomnumber} has been deleted !!!")  # Delete the room from the rooms dictionary
    except ValueError:# Handle invalid input when the user doesn't enter a valid integer
        print("Please enter a valid integer for the room number.")



# Display room detail
"""
    Display the details of a specific room.
    Takes a room number input from the user and shows room type and reservation status.
    """


def room_detail():
    Roomnumber = input("Enter room number too see it information:  ") #Take the room number to see the detail
    Roomnumber = int(Roomnumber)  # May cause valueerror if not int
    if Roomnumber in rooms: # Check if the room number exists in the 'rooms' dictionary
        room = rooms[Roomnumber]# Retrieve the room details
        reservationstatus = "allocated" if room["allocated"] else "Available"
        # Display room details to the user
        print(f"Room number {Roomnumber} - Type: {room['RoomType']} - Status: {reservationstatus}")
    else:
         print("Room not found")# Inform the user if the room number is not found




# Function to reserve a room, scenario customer want to book a room
"""
    Reserve a room if it's available.
    Takes room number input and checks if it's reserved or not. If not reserved, it reserves the room.
    """


def room_allocation():
    try:
        # Prompt the user to enter the room number they want to allocate
        Roomnumber = int(input("Enter room number you want to allocate:  "))
        # Check if the room number exists in the 'rooms' dictionary
        if Roomnumber in rooms:
            if not rooms[Roomnumber]["allocated"]:
                rooms[Roomnumber]["allocated"] = True  # Allocate the room by setting its 'allocated' status to True
                print(f"Room number {Roomnumber} has been allocated.")
            else:
                print("Room already allocated !!!")  # Inform the user that the room is already allocated
        else:
            print(
                "Room not found !!! Double-check your room number.")  # Inform the user if the room number is not found in the records
    except ValueError:
        # This will catch errors if the input is not an integer
        print("Invalid input! Please enter a valid room number (integer).")
    except Exception as e:
        # Catch all other exceptions and print the error message
        print(f"An error occurred: {e}")


#Display room allocation details
"""
    Display the reservation details of all rooms.
    Lists each room with its allocation status (reserved or available).
    """


def allocation_detail():
    try:
        print("Allocation details:")
        # Check if 'rooms' exists and is a dictionary
        if not isinstance(rooms, dict):
            raise ValueError("'rooms' is not defined as a dictionary")
        # Iterate over all room numbers and their details in the 'rooms' dictionary
        for Roomnumber, details in rooms.items():
            # Determine the reservation status based on the 'allocated' key
            reservationdetails = "allocated" if details["allocated"] else "Still Available"
            print(f"Room number {Roomnumber} is {reservationdetails}")
    except KeyError:
        print("Error: The 'allocated' key is missing in the room details.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function for billing and de-allocation
"""
    Process billing and de-allocate a room.
    Takes room number as input, checks if the room is reserved, then processes the billing and marks it as available.
    """


def billing_and_deallocation():
    try:
        # Take Room number input
        Roomnumber = int(input("Enter room number you want to bill and de-allocate"))
        # Take usage time
        print("Please type check-in and check-out time by the following format: 'YYYY-MM-DD HH:MM'")
        check_in_time_str  = input("Enter check-in time: ")
        check_out_time_str = input("Enter check-out time: ")
        # Convert input str into day time
        checkintime = datetime.strptime(check_in_time_str, "%Y-%m-%d %H:%M")
        checkouttime = datetime.strptime(check_out_time_str, "%Y-%m-%d %H:%M")
        if checkouttime <= checkintime: # Make sure check in time must be over check out time
            print("Check out time must be after check in time")
            return
        totaltime = checkouttime - checkintime
        total_hours = totaltime.total_seconds() / 3600
        total_price = rooms[Roomnumber]['Price'] * (total_hours / 24)
        days = int(total_hours // 24) # Calculate the day
        hours = int(total_hours % 24) # Calculate the hours
        print(f"Room number {Roomnumber} is billed for {days} days and {hours} hours.")
        print(f"The total price is: ${total_price:.2f}")
        rooms[Roomnumber]["allocated"] = False
        print(f"Room number {Roomnumber} has been de-allocated.")
    except ValueError:
        print("Invalid input. Please ensure dates are in the format 'YYYY-MM-DD HH:MM'.")


# Exiting the application
def exittheapp():
    print("Exit the app !")
    exit()


# Application Main menu
"""
    Main menu of the application.
    Provides options for adding, deleting, reserving rooms, and other functions.
    Repeats the menu until the user selects the option to exit.
    """


def main_menu(): # The menu of the application
    while True:
        print("*****************************************************************")
        print("\n***Hotel Management Application***")
        print("1. Add Room !")
        print("2. Delete Room !")
        print("3. Display room detail !")
        print("4. Room Reservation !")
        print("5. Display Room Reservation Detail !")
        print("6. Room Billing and De-allocate !")
        print("7. Save room allocation to a file !")
        print("8. Show room allocation from file !")
        print("9. Back up room allocation file")
        print("10. Exit the appication !")
        print("\n*****************************************************************")
        try:
            choice = int(input("What function you want to operate ?:"))
            if choice == 1:
                addroom()
            elif choice == 2:
                delete_room()
            elif choice == 3:
                room_detail()
            elif choice == 4:
                room_allocation()
            elif choice == 5:
                allocation_detail()
            elif choice == 6:
                billing_and_deallocation()
            elif choice == 7:
                save_room_allocation_to_file()
            elif choice == 8:
                show_room_allocation_from_a_file()
            elif choice == 9:
                backup_room_allocation()
            elif choice == 10:
                exittheapp()
            else:
                print("Valid number, double check your choice !!!")
        except ValueError:
            print("Please enter valid number")

# Run the main menu when the script is executed


if __name__ == "__main__":
    main_menu()
