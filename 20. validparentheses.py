class Solution:
    # @return a boolean
	def isValid(self, s):
		leftP = ['(',  '{', '[' ]
		rightP = [')', '}', ']']
		stack = []
		for char in s:
			if char in leftP:
				stack.append(char)
			elif char in rightP:
				if len(stack) == 0:
					return False
				left = stack.pop()
				if leftP.index(left) != rightP.index(char):
					return False
			else:
				return False
		return len(stack) == 0

		

if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	print sol.isValid("()())")
