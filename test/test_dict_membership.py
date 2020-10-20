import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
	def test_in_dict_true(self):
		self.assertEqual(True, dict_membership.in_dict('A', {'A':90, 'B':34}))

	def test_in_dict_false(self):
		self.assertEqual(False, dict_membership.in_dict('A', {'C':90, 'B':34}))


if __name__ == '__main__':
	unittest.main()
