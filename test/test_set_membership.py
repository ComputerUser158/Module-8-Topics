import unittest
from more_fun_with_collections import set_membership


class MyTestCase(unittest.TestCase):
	def test_in_set_true(self):
		self.assertEqual(True, set_membership.in_set(str(3), set('123')))

	def test_in_set_false(self):
		self.assertEqual(False, set_membership.in_set(str(5), set('123')))


if __name__ == '__main__':
	unittest.main()
