"""
Author:Rawley Collins
Program: update_scores_dict.py

"""
MIN = 0
MAX = 100


def get_test_scores():
	scores_dict = dict()
	try:
		num_scores = int(input("How many scores would you like to enter: "))
		if MIN > num_scores:
			raise ValueError
	except ValueError:
		raise ValueError

	for num in range(num_scores):
		flag = False
		while not flag:
			try:
				your_score = float(input("enter score {}:".format(num+1)))
				if MIN < your_score < MAX:
					scores_dict.update({str(num+1):your_score})
					flag = True
				else:
					raise ValueError
			except ValueError:
				print("enter a valid score between {} and {}".format(MIN, MAX))
	return scores_dict


def average_scores(scores):
	total = 0
	for key in scores:
		total += scores[key]
	average = total/len(scores)
	return average


if __name__ == '__main__':
	try:
		my_scores = get_test_scores()
		print("My average is {}".format(average_scores(my_scores)))
	except ValueError:
		print("enter an integer")
