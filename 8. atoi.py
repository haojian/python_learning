class Solution:
    # @return an integer
    def atoi(self, str):
		INT_MAX = 2147483647
		INT_MIN = -2147483648
		str = str.strip()
		if len(str) == 0:
			return 0
		sign = 1
		if str[0] == '-':
			str = str[1:]
			sign = -1
		elif str[0] == '+':
			str = str[1:]
		res = 0
		for idx, char in enumerate(str):
			if str[idx] >= '0' and str[idx] <= '9':
				res = int(str[idx]) + res * 10
			else:
				break
		res *= sign
		if res >= INT_MAX:
			return INT_MAX
		elif res <= INT_MIN:
			return INT_MIN
		return res 
		
		
if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	# print sol.atoi("-123")
	# print sol.atoi("-123ab123")
	print sol.atoi("-2147483648")
