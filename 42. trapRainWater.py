class Solution:
    # @param A, a list of integers
    # @return an integer
	def trap(self, A):
		if len(A) <= 1:
			return 0
		maxR = [0] * len(A)
		maxL = [0] * len(A)
		maxVal = A[0]
		for idx in range(1, len(A)):
			maxL[idx] = maxVal
			if maxVal < A[idx]:
				maxVal = A[idx]
		maxVal = A[len(A)-1]
		for idx in range(len(A)-2, -1, -1):
			maxR[idx] = maxVal
			if maxVal < A[idx]:
				maxVal = A[idx]
		area = 0
		for idx in range(0, len(A)):
			bound = min(maxR[idx], maxL[idx])
			area += max(bound - A[idx], 0)
		return area
			
		
if __name__ == "__main__":
	test = [0,1,0,2,1,0,1,3,2,1,2,1]
	# test = [4,2,3]
	sol = Solution()
	print sol.trap(test)