import unittest
import csv
from getLowestRental import getLowestRental


class TestGetLowestRental(unittest.TestCase):

    def setUp(self):
        print("\ntestSetup")
        with open('testDataset.csv', 'r', newline="") as csvfile:
            self.reader = list(csv.DictReader(csvfile))

    def test_getLowestRental(self):
        print("\ntestingFunc")

        listOfRentals = getLowestRental(self.reader, 1)
        self.assertEqual(len(listOfRentals), 1)
        listOfRentals = getLowestRental(self.reader, 5)
        self.assertEqual(len(listOfRentals), 5)
        listOfRentals = getLowestRental(self.reader, 5)
        print(listOfRentals[0])
        self.assertEqual(listOfRentals[0],
                         {'Property Name': 'Potternewton Crescent',
                          'Property Address [1]': 
                            'Potternewton Est Playing Field',
                          'Property  Address [2]': '',
                          'Property Address [3]': '',
                          'Property Address [4]': 'LS7',
                          'Unit Name': 'Potternewton Est Playing Field',
                          'Tenant Name': 'Arqiva Ltd',
                          'Lease Start Date': '24 Jun 1999',
                          'Lease End Date': '23 Jun 2019',
                          'Lease Years': '20',
                          'Current Rent': '6600.00'})

        with self.assertRaises(ValueError):
            getLowestRental(self.reader, 0)
        with self.assertRaises(ValueError):
            getLowestRental(self.reader, -1)
        with self.assertRaises(TypeError):
            getLowestRental(self.reader, 'one')
        with self.assertRaises(TypeError):
            getLowestRental(self.reader, 1.5)
        with self.assertRaises(IndexError):
            getLowestRental(self.reader, 67)


if __name__ == '__main__':
    unittest.main()
