import csv
from functools import partial

from modules.getRentalTotalWithLease import getRentalTotalWithLease
from modules.getLowestRental import getLowestRental
from modules.mastsOwnedPerTenant import mastsOwnedPerTenant
from modules.rentalsForDateRange import rentalsForDateRange

if __name__ == '__main__':
    with open('dataset.csv', 'r', newline="") as csvfile:
        reader = list(csv.DictReader(csvfile))

    if reader is not None:
        # load all functions here
        if reader is not None:
            func_dict = {1: partial(getRentalTotalWithLease, reader=reader, years=25), 2: partial(getLowestRental, reader, 5),\
                        3: partial(mastsOwnedPerTenant, reader), 4: partial(rentalsForDateRange, reader, '01 Jun 1999', '31 Aug 2007')}

            choice = int(input("Choose run method: \nType 1 to run all with default settings,\
                \nType 2 to select section to run with default settings\n"))

            while choice not in [1, 2]:
                choice = int(input("Try Again\n"))
            # run all
            if choice == 1:
                for i in func_dict:
                    print(func_dict[i]())
            # run selected
            elif choice == 2:
                selectOpt = int(input("Select a option(Type the number):\
                    \n1. Rental Total with lease,\
                    \n2. Five Lowest Rentals,\
                    \n3. Masts owned per tenant,\
                    \n4. Rentals in a date range\n"))
                while selectOpt not in [1, 2, 3, 4]:
                    selectOpt = int(input("Try Again\n"))
                print(func_dict[selectOpt]())

        # Used for testing
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

        # print("Enter a Start Date for rentals within that range(Format: 01 Jan 1990): ")
        # startDate = input()
        # print("Enter a End Date for rentals within that range(Format: 01 Jan 1990): ")
        # endDate = input()
        # listOfDates = rentalsForDateRange(reader, startDate, endDate)

        # # Change date format to 01/01/1990
        # for date in listOfDates:
        #     date["Lease Start Date"] = datetime.strftime(datetime.strptime(
        #     date["Lease Start Date"], '%d %b %Y'), '%d/%m/%Y')

        #     date["Lease End Date"] = datetime.strftime(datetime.strptime(
        #     date["Lease End Date"], '%d %b %Y'), '%d/%m/%Y')
        # print(listOfDates)
else:
    raise KeyError("Could not load the file or read as Dictionary")
