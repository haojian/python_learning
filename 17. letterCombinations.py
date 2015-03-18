class Solution:
    # @return a list of strings, [s1, s2]
	
	def letterCombinations(self, digits):
		if len(digits) == 0:
			return []
		res = [""]
		self.letterCombRecur(digits, res)
		return res
		
	def letterCombRecur(self, digits, res):
		if len(digits) == 0:
			return
		dig_dict = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
		tmpres = res[:]
		res[:] = []
		s_map = dig_dict[int(digits[0])]
		for char in s_map:
			for single_str in tmpres:
				res.append(single_str+char)
		self.letterCombRecur(digits[1:], res)
		
if __name__ == "__main__":
	sol = Solution()
	print sol.letterCombinations("23")