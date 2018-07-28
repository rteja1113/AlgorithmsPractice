"""
Given 2 sequences find the longest common subsequence
A sequence is a subsequence of another sequence if it is a subset in an increasing order of indices
of the sequence. Find longest one of all subsequences that are common to 2 given strings, hence the name
longest common subsequence
"""

def lcs(X, Y):
	"""
	Bottom Up approach, see clrs for how to solve
	"""
	m = len(X)
	n = len(Y)
	seq_lengths = []
	solutions = []

	### Table initialization for bottom up approach ###
	
	# initialize table for saving LCS lengths
	for i in range(m+1):
		seq_lengths.append([])

	for i in range(m+1):
		for j in range(n+1):
			seq_lengths[i].append(-float("Infinity"))

	# initialize table for constructing solutions
	for i in range(m):
		solutions.append([])

	for i in range(m):
		for j in range(n):
			solutions[i].append("")


	# If one of the sequence is of length 0, then LCS length is 0
	for i in range(m+1):
		seq_lengths[i][0] = 0

	for j in range(n+1):
		seq_lengths[0][j] = 0

	# table filling
	for i in range(1, m+1):
		for j in range(1, n+1):
			
			# Xn = Ym = Zk, then Z0..Zk-1 is the LCS of X0...Xm-1, Y0...Yn-1
			# hence you add + 1 to the previous LCS
			if X[i-1] == Y[j-1]:
				seq_lengths[i][j] = seq_lengths[i-1][j-1] + 1
				solutions[i-1][j-1] = "north_west"
			# if not, then you consider max(LCS(X0...Xm-1, Y0...Yn),LCS(X0...Xm, Y0...Yn-1)) 
			else:
				if seq_lengths[i-1][j] < seq_lengths[i][j-1]:
					seq_lengths[i][j] = seq_lengths[i][j-1]
					solutions[i-1][j-1] = "west"
				else:
					seq_lengths[i][j] = seq_lengths[i-1][j]
					solutions[i-1][j-1] = "north"

	return seq_lengths, solutions


def print_lcs(solutions, X, i, j):	
	"""
	Look clrs for explanation
	"""

	if (i == -1) or (j == -1):
		return

	if solutions[i][j] == "north_west":
		print_lcs(solutions, X, i-1, j-1)
		print(X[i], end='', flush=True)
	
	elif solutions[i][j] == "north":
		print_lcs(solutions, X, i-1, j)
	else:
		print_lcs(solutions, X, i, j-1)


def main():
	A = "ABCBDAB"
	B = "BDCABA"
	cs_lengths, solutions = lcs(A, B)
	print_lcs(solutions, A, len(A)-1, len(B)-1)


if __name__ == '__main__':
	main()