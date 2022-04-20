import csv


from modules.getRentalTotalWithLease import getRentalTotalWithLease

if __name__ == '__main__':
    with open('dataset.csv', 'r', newline="") as csvfile:
        reader = list(csv.DictReader(csvfile))

    if reader is not None:
        print("Enter Lease number to get rental total for it: ")
        lease = input()
        print("Rental total for lease of {lease}: ".format(lease=lease) + str(getRentalTotalWithLease(reader, int(lease))))