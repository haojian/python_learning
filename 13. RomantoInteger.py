class Solution:
    # @return an integer
    def romanToInt(self, s):
		chars	= ['I', 'V', 'X', 'L', 'C', 'D', 'M']
		vals	= [1, 	 5,   10,  50,  100, 500, 1000]
		res = 0
		for idx, x in enumerate(s):
			curIdx = chars.index(x)
			if idx < len(s)-1:
				nxtChar = s[idx+1]
				nxtIdx = chars.index(nxtChar)
				if curIdx < nxtIdx:
					res -= vals[curIdx]
					continue
			res += vals[curIdx]
		return res

if __name__ == "__main__":
	sol = Solution()
	print sol.romanToInt('X')
