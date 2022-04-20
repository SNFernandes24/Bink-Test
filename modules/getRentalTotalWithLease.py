def getRentalTotalWithLease(reader, years):
    """

    years: select the specific number of Lease Years to add rental together.

    """
    if isinstance(years, int) is False:
        raise TypeError("Expecting Integer type value")

    # list comprehension to get all data with specified years
    listCompres = [row for row in reader if row["Lease Years"] == str(years)]
    totalRental = 0
    if len(listCompres) > 0:
        for currRent in listCompres:
            totalRental += float(currRent["Current Rent"])
            print(currRent)
    else:
        raise ValueError("Specified Year does not exist")

    return totalRental
