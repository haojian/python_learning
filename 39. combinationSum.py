class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
	def combinationSum(self, candidates, target):
		res = []
		candidates.sort()
		self.combRecur(candidates, 0, [], target, res)
		return res
		
	def combRecur(self, candidates, si, curRes, target, res):
		if target < 0:
			return
		if target == 0 and curRes not in res:
			res.append((list(curRes)))				
			return
		for idx in range(si, len(candidates)):
			curRes.append( candidates[idx] )
			self.combRecur(candidates, idx, curRes, target-candidates[idx], res)
			curRes.pop()

		
if __name__ == "__main__":
	sol = Solution()
	print sol.combinationSum(	[8,7,4,3], 11)