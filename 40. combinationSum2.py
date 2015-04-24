import time

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
	def combinationSum2(self, candidates, target):
		res = []
		candidates.sort()
		self.combRecur(candidates, 0, [], target, res)
		return res
		
	def combRecur(self, candidates, si, curRes, target, res):
		if target < 0:
			return
		if target == 0 and curRes not in res:
			res.append(curRes[:])				
			return
		for idx in range(si, len(candidates)):
			if idx > 0 and candidates[idx] == candidates[idx-1] and candidates[idx] not in curRes:
				continue
			curRes.append( candidates[idx] )
			self.combRecur(candidates, idx+1, curRes, target-candidates[idx], res)
			curRes.pop()

		
if __name__ == "__main__":
	sol = Solution()
	t0 = time.time()
	print sol.combinationSum2([13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19], 25)
	t1 = time.time()
	print t1-t0