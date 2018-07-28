
def merge(A, left, middle, right):
	"""
	Merges 2 sorted arrays
	"""
	L1 = []
	L2 = []

	for i in range(left, middle+1):
		L1.append(A[i])

	for i in range(middle+1, right+1):
		L2.append(A[i])

	i = 0
	j = 0
	k = left
	
	while i < len(L1) and j < len(L2):
		if L1[i] < L2[j]:
			A[k] = L1[i]
			i += 1
		else:
			A[k] = L2[j]
			j += 1
		k += 1

	while i < len(L1):
		A[k] = L1[i]
		i += 1
		k += 1

	while j < len(L2):
		A[k] = L2[j]
		j += 1
		k += 1

	return 


def merge_sort(A, left, right):
	"""
	Merge Sort implementation
	"""

	if left < right:
		middle = (left + right)//2
		merge_sort(A, left, middle)
		merge_sort(A, middle+1, right)
		merge(A, left, middle, right)


def main():
	A = [3, 1, 2, 10, 7]
	merge_sort(A, 0, len(A)-1)
	print(A)


if __name__ == '__main__':
	main()
