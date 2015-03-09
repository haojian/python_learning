# Given an array of integers, find two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution.
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2


class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		map = {}
		for i in range(0, len(num)):
			if map.has_key(target-num[i]):
				return (map[target-num[i]]+1, i+1)
			else:
				map[num[i]] = i
				
	def twoSum_v1(self, num, target):
		map = {}
		for idx, val in enumerate(num):
			if target-val in map:
				return (map[target-val]+1, idx+1)
			else:
				map[val] = idx

if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	print sol.twoSum([1, 2], 3)
	print sol.twoSum_v1([1, 2], 3)