import csv


from modules.getRentalTotalWithLease import getRentalTotalWithLease
from modules.getLowestRental import getLowestRental
from modules.mastsOwnedPerTenant import mastsOwnedPerTenant

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
        
        print("Amount of Masts owned per tenant: ")
        print(mastsOwnedPerTenant(reader))