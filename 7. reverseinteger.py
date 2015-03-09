class Solution:
	# @return an integer
	def reverse(self, x):
		sign = 1
		if x < 0:
			sign = -1
			x = -x
		res = 0
		while x > 0:
			res = x%10+res*10
			x = x/10
		if -2147483648L <= res <= 2147483647L:   
			return res * sign
		else:
			return 0
