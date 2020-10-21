import unittest
from datetime import datetime
from more_fun_with_collections import six_months


class MyTestCase(unittest.TestCase):
	def test_half_birthday(self):
		self.assertEqual(datetime(2003, 12, 1), six_months.half_birthday(datetime(2003, 6, 1)))


if __name__ == '__main__':
	unittest.main()
