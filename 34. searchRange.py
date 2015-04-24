from bisect import bisect_left, bisect_right

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
	def searchRange(self, A, target):
		li = bisect_left(A, target)
		print li
		li = li if li != len(A) and A[li] == target else -1
		ri = bisect_right(A, target)
		ri = ri if ri != 0 and A[ri-1] == target else -1
		if ri == -1 or li == -1:
			return [-1, -1]
		return [li, ri-1]
		
if __name__ == "__main__":
	sol = Solution()
	print sol.searchRange([5, 7, 7, 8, 8, 8, 9, 10], 8)
		
