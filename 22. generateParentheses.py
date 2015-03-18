class Solution:
    # @param an integer
    # @return a list of string
	def generateParenthesis(self, n):
		if n == 0:
			return []
		res = []
		self.genRecur(res, '(', n-1, n)
		return res
		
		
	def genRecur(self, res, str, left, right):
		if left > right or left < 0 or right < 0:
			return
		if left == 0 and right == 0:
			res.append(str)
		self.genRecur(res, str+')', left, right-1)
		self.genRecur(res, str+'(', left-1, right)
		

if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	print sol.generateParenthesis(3)