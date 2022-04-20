import unittest
import csv
from getRentalTotalWithLease import getRentalTotalWithLease


class TestGetRentalTotalWithLease(unittest.TestCase):

    # Set up class
    def setUp(self):
        print("\ntestSetup")
        with open('testDataset.csv', 'r', newline="") as csvfile:
            self.reader = list(csv.DictReader(csvfile))

    # Test if equal
    def test_equalGetRentalTotalWithLease(self):
        totalRental = getRentalTotalWithLease(self.reader, 25)
        self.assertEqual(totalRental, 46500)
        totalRental = getRentalTotalWithLease(self.reader, 64)
        self.assertEqual(totalRental, 23950)

    # Test for value error
    def test_valueErrGetRentalTotalWithLease(self):
        with self.assertRaises(ValueError):
            getRentalTotalWithLease(self.reader, 73)

    # Test for type error
    def test_typeErrGetRentalTotalWithLease(self):
        with self.assertRaises(TypeError):
            getRentalTotalWithLease(self.reader, '73')


if __name__ == '__main__':
    unittest.main()
