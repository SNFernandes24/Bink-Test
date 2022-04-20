import csv
from datetime import datetime

from modules.getRentalTotalWithLease import getRentalTotalWithLease
from modules.getLowestRental import getLowestRental
from modules.mastsOwnedPerTenant import mastsOwnedPerTenant
from modules.rentalsForDateRange import rentalsForDateRange

if __name__ == '__main__':
    with open('dataset.csv', 'r', newline="") as csvfile:
        reader = list(csv.DictReader(csvfile))

    if reader is not None:
        # print("Enter Lease number to get rental total for it: ")
        # lease = input()
        # print("Rental total for lease of {lease}: ".format(lease=lease) + str(getRentalTotalWithLease(reader, int(lease))))
        
        # print("Enter the number of lowest rentals to fetch: ")
        # count = input()
        # listOfRentals = getLowestRental(reader, int(count))
        # print("{count} lowest rentals: ".format(count=count))
        # for rental in listOfRentals:
        #     print(rental)
        
        # print("Amount of Masts owned per tenant: ")
        # print(mastsOwnedPerTenant(reader))

        print("Enter a Start Date for rentals within that range(Format: 01 Jan 1990): ")
        startDate = input()
        print("Enter a End Date for rentals within that range(Format: 01 Jan 1990): ")
        endDate = input()
        listOfDates = rentalsForDateRange(reader, startDate, endDate)

        # Change date format to 01/01/1990
        for date in listOfDates:
            date["Lease Start Date"] = datetime.strftime(datetime.strptime(
            date["Lease Start Date"], '%d %b %Y'), '%d/%m/%Y')

            date["Lease End Date"] = datetime.strftime(datetime.strptime(
            date["Lease End Date"], '%d %b %Y'), '%d/%m/%Y')
        print(listOfDates)
else:
    raise KeyError("Could not load the file or read as Dictionary")
