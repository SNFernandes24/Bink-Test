import unittest
import csv
from getRentalTotalWithLease import getRentalTotalWithLease


class TestGetRentalTotalWithLease(unittest.TestCase):

    def setUp(self):
        print("\ntestSetup")
        with open('testDataset.csv', 'r', newline="") as csvfile:
            self.reader = list(csv.DictReader(csvfile))

    def test_getRentalTotalWithLease(self):
        print("\ntestingFunc")

        totalRental = getRentalTotalWithLease(self.reader, 25)
        self.assertEqual(totalRental, 46500)
        totalRental = getRentalTotalWithLease(self.reader, 64)
        self.assertEqual(totalRental, 23950)

        with self.assertRaises(ValueError):
            getRentalTotalWithLease(self.reader, 73)
        with self.assertRaises(TypeError):
            getRentalTotalWithLease(self.reader, '73')


if __name__ == '__main__':
    unittest.main()
