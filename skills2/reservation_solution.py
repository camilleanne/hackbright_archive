"""
Reservation finder

Along with this file, you'll find two files named units.csv and reservations.csv with fields in the following format

units.csv
location_id, unit_size

reservations.csv
location_id, reservation_start_date, reservation_end_date

You will write a simple application that manages a reservation system. It will have two commands, 'available' and 'reserve' with the following behaviors:

available <date> <number of occupants> <length of stay>
This will print all available units that match the criteria. Any unit with capacity equal or greater to the number of occupants will be printed out.

Example:
SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available

reserve <unit number> <start date> <length of stay>
This creates a record in your reservations that indicates the unit has been reserved. It will print a message indicating its success.

A reservation that ends on any given day may be rebooked for the same evening, ie:
    
    If a reservation ends on 10/10/2013, a different reservation may be made starting on 10/10/2013 as well.

Example:
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights

Reserving a unit must make the unit available for later reservations. Here's a sample session:

SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights
SeaBnb> available 10/10/2013 2 4
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Unit 10 is unavailable during those dates
SeaBnb> quit

Notes:
Start first by writing the functions to read in the csv file. These have been stubbed for you. Then write the availability function, then reservation. Test your program at each step (it may be beneficial to write tests in a separate file.) Use the 'reservations' variable as your database. Store all the reservations in there, including the ones from the new ones you will create.

The datetime and timedelta classes will be immensely helpful here, as will the strptime function.
"""

import sys
import datetime

def parse_date(s):
    return datetime.datetime.strptime(s, "%m/%d/%Y")

def parse_one_record(line):
    """Take a line from reservations.csv and return a dictionary representing that record. (hint: use the datetime type when parsing the start and end date columns)"""
    line = line.strip()
    cols = line.split(", ")
    unit_id = int(cols[0])
    start_date = parse_date(cols[1])
    end_date = parse_date(cols[2])
    return {"id": unit_id, "start_date": start_date, "end_date": end_date}

def read_units():
    """Read in the file units.csv and returns a list of all known units."""
    units = []
    f = open("units.csv")
    for line in f:
        cols = line.split(", ")
        units.append({"id": int(cols[0].strip()), 
                      "capacity": int(cols[1].strip())})

    return units

def read_existing_reservations():
    """Reads in the file reservations.csv and returns a list of reservations."""
    reservations = []

    f = open("reservations.csv")
    for line in f.readlines():
        reservations.append(parse_one_record(line))    

    f.close()
    print reservations
    return reservations


def overlap(start1, end1, start2, end2):
    # De morgan's law is cool
    return start2 < end1 and start1 < end2

def available(units, reservations, start_date, occupants, stay_length):
    end_date = parse_date(start_date) + datetime.timedelta(days=int(stay_length))
    unavailable = []
    for r in reservations:
        if overlap(start_date, end_date, r['start_date'], r['end_date']):
            unavailable.append(r['id'])

    print "Unit %d is available"%unit_id

def reserve(units, reservations, unit_id, start_date, stay_length):
    print "Successfully reserved"

def main():
    units = read_units()
    print units
    reservations = read_existing_reservations()  
    print reservations

    while True:
        command = raw_input("SeaBnb> ")
        cmd = command.split()
        if cmd[0] == "available":
            # look up python variable arguments for explanation of the *
            available(units, reservations, *cmd[1:])
        elif cmd[0] == "reserve":
            reserve(units, reservations, *cmd[1:])
        elif cmd[0] == "quit":
            sys.exit(0)
        elif cmd[0] == "/":
            print "Hello"
        else:
            print "Unknown command"

if __name__ == "__main__":
    main()
