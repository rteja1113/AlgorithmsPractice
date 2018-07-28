"""
The classic 0/1  Knapsack. Given a limited number of items
with their corresponding weights and values, maximize the value of the bag which can carry upto a total weight of W.
No breaking of the items into pieces. Either you take it or don't(hence the 0/1)
"""



def knap_sack(values, weights, W, n, sack):
	"""
	Top Down Approach 
	"""

	if (n == 0) or (W == 0):
		return 0

	

	# if the nth item is larger than W, then	
	# the solution is the same with n-1 items, since
	# you can't add the n'th item
	if weights[n-1] > W:
		return knap_sack(values, weights, W, n-1)
	else:
		# if not consider the max of including the item v.s not 
		# including the item 
		include_nth = values[n-1] + knap_sack(values, weights, W - weights[n-1], n-1)
		not_include_nth = knap_sack(values, weights, W, n-1)
		if (include_nth > not_include_nth):
			max_sack = include_nth 
		else:
			max_sack = not_include_nth

		return max_sack


def main():
	values = [60, 100, 120]
	weights = [10, 20, 30]
	W = 50
	n = len(values)
	
	print(knap_sack(values, weights, W, n)
	print("The items to consider are : ", sack)


if __name__ == '__main__':
	main()