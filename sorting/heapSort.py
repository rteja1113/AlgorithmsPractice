
def left(i):
	"""
	returns left child
	"""
	return 2*i + 1


def right(i):
	"""
	returns right child
	"""
	return 2*(i+1)


def max_heapify(A, i):
	"""
	max-heapifies if a node violates max-heap property 
	by trickling it down
	"""

	l = left(i)
	r = right(i)
	largest = i
	if l < len(A) and A[l] > A[i]:
		largest = l
	
	if r < len(A) and A[r] > A[largest]:
		largest = r

	if largest != i:
		# swap largest with i
		temp = A[i]
		A[i] = A[largest]
		A[largest] = temp
		max_heapify(A, largest)


def build_max_heap(A):
	"""
	Builds a max heap given a random array
	"""
	n = len(A)
	for i in range(n//2, -1, -1):
		max_heapify(A, i)


def extract_max(A):
	"""
	Swaps max with leaf and pops it.
	"""

	temp = A[len(A)-1]
	A[len(A)-1] = A[0]
	A[0] = temp
	return A.pop()


def heap_sort(A):
	"""
	Heap Sort implementation
	"""
	build_max_heap(A)
	while(len(A) > 0):
		max_element = extract_max(A)
		max_heapify(A, 0)
		print(max_element)


def main():
	A = [3, 1, 2, 4, 5]
	heap_sort(A)


if __name__ == '__main__':
	main()
