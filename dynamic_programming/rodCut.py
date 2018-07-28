"""
We can cut up a rod of length n in 2^(n-1) different ways, since we have an in-
dependent option of cutting, or not cutting, at distance i inches from the left end,
"""

def memoized_cut_rod(prices, n):
	"""
	Top Down Approach
	"""
	revenues = [-float("Infinity")]*(n+1)
	return revenues, memoized_cut_rod_aux(prices, n, revenues)	


def memoized_cut_rod_aux(prices, n, r):
	"""
	Recursive function for calculating
	solutions for sub-problems and saving them.
	"""

	if r[n] >= 0:
		return r[n]
	if n == 0:
		return 0
	else:
		q = -float("Infinity")
		for i in range(n):
			q = max(q, prices[i] + memoized_cut_rod_aux(prices, (n-1)-i, r))
		r[n] = q
		return q


def bottom_up_cut_rod(p, n):
	revenues = [-float("Infinity")]*(n+1)
	revenues[0] = 0

	for i in range(1, n+1):
		q = -float("Infinity")
		for j in range(i):
			q = max(q, p[j] + revenues[i-j-1])
		revenues[i] = q
	return revenues


def extending_bottom_up_cut_rod(p, n):
	revenues = [-float("Infinity")]*(n+1)
	revenues[0] = 0
	solutions = [0]*(n+1)

	for i in range(1, n+1):
		q = -float("Infinity")
		for j in range(i):
			if q < p[j] + revenues[i-j-1]:
				q = p[j] + revenues[i-j-1]
				solutions[i] = j

		revenues[i] = q
	return revenues, solutions


def main():
	length = 10
	prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
	print("Top-Down Approach: ", memoized_cut_rod(prices, 10))
	print("Bottom-Up Approach: ", bottom_up_cut_rod(prices, length))
	print("Bottom-Up Approach with cuts: ", extending_bottom_up_cut_rod(prices, length))


if __name__ == '__main__':
	main()