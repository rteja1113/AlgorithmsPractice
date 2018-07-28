"""
Given a finite set of unique denominations, find the minimum number of coins 
you need to make up an amount A. You have unlimited access to the number of coins
"""
def coin_change(denominations, amount, solutions):
	if amount == 0:
		return 0
	
	if amount in solutions:
		return solutions[amount]
	else:
		placeholder = float("Infinity")
		for d in denominations:
			if amount - d >= 0:
				q = coin_change(denominations, amount - d, solutions)+1
				if q < placeholder:
					placeholder = q
					solutions[amount] = placeholder # memoization
				
				
		return placeholder


def main():
	denominations =[1, 2, 5]
	amount = 35
	solutions = {}

	print(coin_change(denominations, amount, solutions))


if __name__ == '__main__':
	main()



