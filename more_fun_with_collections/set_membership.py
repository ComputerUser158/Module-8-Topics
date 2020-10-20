"""
Author: Rawley Collins
Program: set_membership.py

"""


def in_set(some_input, some_set):
	return some_input in some_set


if __name__ == '__main__':
	test_var = 56
	my_set = set('123467')
	print("Is {} in {}, {}".format(test_var, my_set, in_set(str(test_var), my_set)))
