"""
Author:Rawley Collins
Program: assign_average.py

"""


def switch_average(entry):
	my_dict = {'A': "You entered an A!",
			   'B': 'You entered an B!',
			   'C': 'You entered an C!',
			   'D': 'You entered an D!'}
	return my_dict.get(entry)


if __name__ == '__main__':
	print(switch_average('A'))
