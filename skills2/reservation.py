
import sys
import datetime
import csv
import time
import datetime

# ['6', ' 9/27/2013', ' 12/1/2013']
def parse_date(string):
    return datetime.datetime.strptime(string, "%m/%d/%Y")

def parse_one_record(line):
    """Take a line from reservations.csv and return a dictionary 
    representing that record. """
    unit_id = int(line[0])
    reservation_dates = line[1:]
    for i in range(len(reservation_dates)):
        reservation_dates[i] = reservation_dates[i].strip()
        reservation_dates[i] = parse_date(reservation_dates[i])
    start_date = reservation_dates[0]
    end_date = reservation_dates[1]

    return {"id": unit_id, "start_date": start_date, "end_date": end_date}

def read_units():
    """Read in the file units.csv and returns a list of all known units."""
    units = []
    with open('units.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        for row in reader:

            units.append({"id": int(row[0].strip()), 
                      "capacity": int(row[1].strip())})
    return units

def read_existing_reservations():
    """Reads in the file reservations.csv and returns a list of reservations."""
    # as list:
    reservations = []
    with open('reservations.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        for row in reader:
            reservations.append(parse_one_record(row))
    return reservations

def available(units, reservations, start_date, occupants, stay_length):
    unavailable = []
    unit_id = 0
    start_date = parse_date(start_date)
    end_date = start_date + datetime.timedelta(days=int(stay_length))
    for r in reservations:
            if start_date < r["end_date"] or r["start_date"] < end_date:
                unavailable.append(r['id'])
    for u in units:
        if u["id"] not in unavailable:
            if u["capacity"] >= int(occupants):
                print "Unit %d is available"%u["id"]


def reserve(units, reservations, unit_id, start_date, stay_length):
    start_date = parse_date(start_date)
    end_date = start_date + datetime.timedelta(days=int(stay_length))
    for r in reservations:
        if r["id"] == int(unit_id) and (start_date < r["end_date"] or r["start_date"] < end_date):
            print "Unit %s is unavailable during those dates" % unit_id
            return
    for u in units:
        if u["id"] == int(unit_id):
            reservations.append({"id": unit_id, "start_date": start_date, "end_date": end_date})
            print "Successfully reserved unit %s for %s nights" % (unit_id, stay_length)
            print reservations
        else:
            print "This unit does not exist. Try another, or try checking availability by date."

def main():
    units = read_units()
    reservations = read_existing_reservations()

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
        else:
            print "Unknown command"

if __name__ == "__main__":
    main()
