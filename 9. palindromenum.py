class Solution:
	# @return a boolean
	def isPalindrome(self, x):
		if x < 0:
			return False
		if x < 10:
			return True
		forward = x
		backward = 0
		while(forward > backward):
			backward = backward*10 + forward%10
			forward /= 10
		if forward == backward or backward/10 == forward:
			return True
		else:
			return False



if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	# print sol.atoi("-123")
	# print sol.atoi("-123ab123")
	print sol.isPalindrome(123)
	print sol.isPalindrome(323)
	print sol.isPalindrome(121)
	print sol.isPalindrome(10)