"""
Author:Rawley Collins
Program: assign_average.py

"""


def switch_average(entry):
	my_dict = {'A': "You entered an A!"}
	return my_dict.get(entry)


if __name__ == '__main__':
	print(switch_average('A'))
