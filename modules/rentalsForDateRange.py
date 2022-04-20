from datetime import datetime


def rentalsForDateRange(reader, start, end):
    """
    start: Specify the start date to limit the data returned.
    end: Specify the end date to limit the data returned.

    """
    if isinstance(start, str) is False:
        raise TypeError("Expecting a String value")
    try:
        datetime.strptime(start, '%d %b %Y')
    except ValueError:
        raise ValueError("Expecting date format: '01 Jan 1990' for Start date")
    try:
        datetime.strptime(end, '%d %b %Y')
    except ValueError:
        raise ValueError("Expecting date format: '01 Jan 1990' for End date")

    sortedList = sorted(reader, key=lambda row: datetime.strptime(
            (row['Lease Start Date']), '%d %b %Y')
        )
    dateInRange = []

    # Expecting '01 Jan 1990' format for date
    for date in sortedList:
        if datetime.strptime(date["Lease Start Date"], '%d %b %Y') >= \
                datetime.strptime(start, '%d %b %Y') and \
                datetime.strptime(date["Lease Start Date"], '%d %b %Y') <= \
                datetime.strptime(end, '%d %b %Y'):

            dateInRange.append(date)
    return dateInRange
