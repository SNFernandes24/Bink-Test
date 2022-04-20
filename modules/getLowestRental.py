def getLowestRental(reader, count):
    """

    count: The rows of data to return.

    """
    # Exception handling
    if isinstance(count, int) is False:
        raise TypeError("Expecting Integer type value")
    if count <= 0:
        raise ValueError("Invalid Operation: Must be greater than 0")
    if count > len(reader):
        raise IndexError("Value is greater than the length of dictionary")

    # sort by current rent
    sortedList = sorted(reader, key=lambda row: float(row['Current Rent']))
    listOfRentals = []
    for i in range(0, count):
        listOfRentals.append(sortedList[i])

    return listOfRentals
