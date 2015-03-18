class Solution:
    # @return a string

	# Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
	# I can only be placed before V and X.
	# X can only be placed before L and C.
	# C can only be placed before D and M.

    def intToRoman(self, num):
		vals	= [1000, 900, 500, 400,  100,  90,  50,  40,   10,   9,    5,   4,    1]
		chars	= ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
		# chars	= ['I', 'V', 'X', 'L', 'C', 'D', 'M']
		# vals	= [1, 	 5,   10,  50,  100, 500, 1000]
		
		res = ''
		for i in range(len(chars)):
			while num/vals[i]:
				res += chars[i]
				num -= vals[i]
		return res
		
if __name__ == "__main__":
	sol = Solution()
	print sol.intToRoman(3999)
	print sol.intToRoman(10)
