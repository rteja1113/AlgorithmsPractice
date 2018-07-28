"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

 
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

def stock_price(array):
	"""
	As it loops through array, it does 2 things

	1) check if current value is smaller than current minimum and update the current minimum
	2) if not check if the difference between current value and current minimum is larger than current max profit
	"""
	min_price = float('Infinity')
	max_profit = 0

	for i in range(len(array)):
		if (array[i] < min_price):
			min_price = array[i]
		elif (array[i] - min_price > max_profit):
			max_profit = array[i] - min_price

	return max_profit


def main():
	prices = [7,1,5,3,6,4]
	print(stock_price(prices))
	
	prices = [7,6,4,3,1]
	print(stock_price(prices))


if __name__ == '__main__':
	main()




