class Solution:
	# k is 1 based.
	def findkthinTwoArray(self, A, B, k):
		if len(A) > len(B):
			return self.findkthinTwoArray(B, A, k)
		if len(A) == 0:
			return B[k-1]
		if k == 1:
			return min(A[0], B[0])
		# print k, len(A), len(B)
		pa = min( k/2, len(A) )
		pb = k - pa
		if A[pa-1] < B[pb-1]:
			return self.findkthinTwoArray(A[pa:], B, k-pa)
		elif A[pa-1] > B[pb-1]:
			return self.findkthinTwoArray(A, B[pb:], k-pb)
		else:
			return A[pa-1]
			
	# @return a float
	def findMedianSortedArrays(self, A, B):
		length = len(A)+len(B)
		if length == 0:
			return 0
		if length % 2:
			return self.findkthinTwoArray(A, B, length/2+1)
		else:
			return float( self.findkthinTwoArray(A, B, length/2) + self.findkthinTwoArray(A, B, length/2+1) )/2
			
			
if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	# print sol.findMedianSortedArrays([1, 2, 3, 4], [4, 5, 5])
	# print sol.findMedianSortedArrays([1, 2], [3, 4, 5])
	# print sol.findMedianSortedArrays([1, 2, 3], [3, 4, 5])
	print sol.findMedianSortedArrays([1, 2, 3, 4], [3, 4, 5])
	print sol.findMedianSortedArrays([1, 2, 3, 4], [5, 6, 7, 7])
	print sol.findMedianSortedArrays([], [2,3])