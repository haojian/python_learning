class Solution:
	# @return a boolean
	def isMatch(self, s, p):
		if len(s) == 0 and len(p) == 0:
			return True
		if len(s) != 0 and len(p) == 0:
			return False
		if len(p) > 1 and p[1] == '*':
			# match 0 char
			match0 = self.isMatch(s, p[2:])
			# match 1 char
			match1 = False
			if self.stepMatch(s, p):
				match1 = self.isMatch(s[1:], p)
			return match0 or match1
		elif self.stepMatch(s, p):
			return self.isMatch(s[1:], p[1:])
		else:
			return False
				
	def stepMatch(self, s, p):
		if len(s) == 0 and len(p) == 0:
			return True
		if len(s) > 0 and len(p) > 0 and (s[0] == p[0] or p[0] == '.'):
			return True
		return False
		
		
	# def isMatch_v1(self, s, p):
	# 	if len(s) == 0 and len(p) == 0:
	# 		return True
	# 	if len(s) != 0 and len(p) == 0:
	# 		return False
	# 	res = False
	# 	if len(p) > 1 and p[1] == '*':
	# 		# match 0
	# 		res = res or self.isMatch(s, p[2:])
	# 		# match 1
	# 		if len(s) != 0 and self.ifCharMatch(s[0], p[0]):
	# 			res = res or self.isMatch(s[1:], p)
	# 		return res
	# 	elif len(s) != 0 and self.ifCharMatch(s[0], p[0]):
	# 		return self.isMatch(s[1:], p[1:])
	# 	else:
	# 		return False
	# 					
	# def ifCharMatch_v1(self, char1, char2):
	# 	if char1 == char2 or char2 == '.':
	# 		return True
	# 	else:
	# 		return False
			
if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	# print sol.atoi("-123")
	# print sol.atoi("-123ab123")
	# print sol.isMatch("aa", "a*")
	# print sol.isMatch("ab", ".*a")
	# print sol.isMatch("a", "ab*")
	print sol.isMatch("aaba", "c*a*b")
	print sol.isMatch("bbbba", ".*a*a")
	