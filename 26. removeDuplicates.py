class Solution:
    # @param a list of integers
    # @return an integer
	def removeDuplicates(self, A):
		#init
		if len(A) == 0:
			return 0
		lastidx = 0
		# print len(A)
		for i in xrange( 1, len(A) ):
			if A[i] == A[lastidx]:
				continue
			else:
				A[lastidx+1] = A[i]	
				lastidx+=1	
		return lastidx+1
		
if __name__ == "__main__":
	sol = Solution()
	print sol.removeDuplicates([1,1,2])
