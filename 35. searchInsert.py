from bisect import bisect_left
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
	def searchInsert(self, A, target):
		idx = bisect_left(A, target)
		return idx
		