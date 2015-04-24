class Solution:
    # @param A, a list of integers
    # @return an integer
	def firstMissingPositive(self, A):
		if len(A) == 0:
			return 1
		cache = [0] * (len(A)+1)
		for val in A:
			if val <=0 :
				continue
			if val > len(A):
				continue
			cache[val] = 1
		for idx in range(1, len(cache)):
			if cache[idx] == 0:
				return idx
		else:
			return len(cache)
		

if __name__ == "__main__":
	sol = Solution()
	print sol.firstMissingPositive([1,2,0])	
	print sol.firstMissingPositive([3,4,-1,1])	
	print sol.firstMissingPositive([2])		
	print sol.firstMissingPositive([1])	