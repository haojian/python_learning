class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integers
	def findSubstring(self, S, L):
		combs = []
		self.getCombination(L, 0, len(L), "", combs)
		res = []
		for comb in combs:
			idx = S.find(comb)
			if idx != -1:
				res.append(idx)
		return res
		
		
	def getCombination(self, L, si, ei, curstr, res):
		if len(L) == 0:
			return
		if si == ei:
			if curstr not in curstr:
				res.append(curstr)
			return
		for idx in range(si, len(L)):
			self.swapValue( L, si, idx )
			self.getCombination(L, si+1, ei, curstr + L[si], res)
			self.swapValue( L, si, idx )


	def swapValue(self, L, li, ri):
		tmp = L[li]
		L[li] = L[ri]
		L[ri] = tmp
		
if __name__ == "__main__":
	sol = Solution()
	print sol.findSubstring("barfoothefoobarman", ["foo", "bar"])