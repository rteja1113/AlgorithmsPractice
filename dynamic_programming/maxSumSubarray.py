"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


def max_sub_array(array):
	sums = [0]*len(array)
	sums[0] = array[0]
	max_sum = array[0]

	for i in range(1, len(array)):
		sums[i] = max(array[i], sums[i-1]+array[i])
		max_sum = max(max_sum, sums[i])
	return max_sum


def main():
	array = [-2,1,-3,4,-1,2,1,-5,4]
	print(max_sub_array(array))

if __name__ == '__main__':
	main()


