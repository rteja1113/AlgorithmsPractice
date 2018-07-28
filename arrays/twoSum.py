"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""



def two_sum(array, target):
	"""
	Uses dictionary to make lookup O(1)
	makes n lookups hence O(n)
	"""

	lookup = {}
	for i in range(len(array)):
		lookup[array[i]] = i

	for i in range(len(array)):
		compliment = target - array[i]
		if (compliment in lookup) and (lookup[compliment] != i): # can't have same number twice
			return (i, lookup[compliment])

	return "Not Present"


def main():
	array = [10, 1, 12, 14, 20]
	target = 26
	print(two_sum(array, target))


if __name__ == '__main__':
	main()