class Solution:
	# @return a boolean
	def isPalindrome(self, x):
		if x < 0:
			return False
		div = 1
		while x/div >= 10:
			div *= 10
		while x:
			left = x / div
			right = x % 10
			if left != right:
				return False
			x = (x % div)/10
			div /= 100
		return True

if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	# print sol.atoi("-123")
	# print sol.atoi("-123ab123")
	print sol.isPalindrome(123)
	print sol.isPalindrome(323)
	print sol.isPalindrome(121)
	print sol.isPalindrome(10)