"""
Author: Rawley Collins
Program: six_months.py

"""
from datetime import datetime, timedelta


def half_birthday(date):
	new_date = date + timedelta(days=183)  # 183 days because months isn't a thing timedelta can do
	return new_date


if __name__ == '__main__':
	my_date = datetime(2003, 6, 1)
	print(half_birthday(my_date))
