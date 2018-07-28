"""
Given dimensions of a sequence of matrices A0, A1, ....
find parenthesizations that minimize number of multiplies
"""
import sys

def initialize(num_matrices, placeholder):
	"""
	Constructs a matrix of dims (num_matrices x num_matrices)
	filled with Infinities
	"""
	ops = []
	for _ in range(num_matrices):
		ops.append([])
	for row in ops:
		for _ in range(num_matrices):
			row.append(placeholder)

	return ops	


def matmul(dims, num_matrices):
	"""
	Top Down approach
	"""
	# initialize the matrix
	ops = initialize(num_matrices, float("Infinity"))
	return matmul_aux(ops, dims, 0, num_matrices-1)
	

def matmul_aux(ops, dims, i, j):
	"""
	Top Down approach recursive function
	"""
	if ops[i][j] < float("Infinity"):
		return ops[i][j]
	
	if i == j:
		return 0
	else:
		for k in range(i, j):
			q = matmul_aux(ops, dims, i, k) + matmul_aux(ops, dims, k+1, j) +  dims[i]*dims[k+1]*dims[j+1]
			if q < ops[i][j]:
				ops[i][j] = q
	
	return ops[i][j]



def maxtrix_chain_order(p):
	"""
	Bottom Up approach
	"""
	num_matrices = len(p) - 1
	ops = initialize(num_matrices, float("Infinity"))
	splits = initialize(num_matrices, float("Infinity"))

	# number of multiplies for chain length 1 is 0
	for i in range(num_matrices):
		ops[i][i] = 0

	# chain length from 2:num_matrices
	for l in range(2, num_matrices+1):
		for i in range(num_matrices-l+1):
			j = i + l - 1
			for k in range(i, j):
				q = ops[i][k] + ops[k+1][j] + p[i]*p[k+1]*p[j+1] 
				if q < ops[i][j]:
					ops[i][j] = q
					splits[i][j] = k
	return ops[0][num_matrices-1], splits


def print_optimal_splits(splits,  i, j):
	"""
	Recursively print optimal parenthisaztion
	"""
	if i == j:
		print('A{}'.format(i), end='', flush=True)
	else:
		print("(", end='', flush=True)
		print_optimal_splits(splits, i, splits[i][j])
		print_optimal_splits(splits, splits[i][j]+1, j) 
		print(")", end='', flush=True)


def main():
	dims = [30, 35, 15, 5, 10, 20, 25]
	
	# Top Down 
	print(matmul(dims, len(dims)-1))
	
	# Bottom Up
	min_ops, splits = maxtrix_chain_order(dims)
	print("min operations : ", min_ops)
	print_optimal_splits(splits, 0, len(dims)-2)

if __name__ == '__main__':
	main()