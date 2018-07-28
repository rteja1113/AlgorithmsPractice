"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def check_duplicates(array):
	"""
	Takes advantage of dictionary's collision property
	"""
	lookup = {}
	for i in range(len(array)):
		if array[i] in lookup:
			lookup[array[i]] = lookup[array[i]] + 1
		else:
			lookup[array[i]] = 1

	for key, value in lookup.items():
		if value > 1:
			return True

	return False


def main():
	array = [1,2,3,4]
	print(check_duplicates(array))
	
	array = [1,1,1,3,3,4,3,2,4,2]
	print(check_duplicates(array))


if __name__ == '__main__':
	main()



