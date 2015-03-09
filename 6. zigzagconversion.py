class Solution:
    # @return a string
    def convert(self, s, nRows):
		if nRows == 1:
			return s
		tmp = ['' for i in range(nRows)]
		idx = 0
		step = 1
		for i, char in enumerate(s):
			if idx == nRows-1:
				step = -1
			elif idx == 0:
				step = 1
			tmp[idx] += char
			idx += step
		return ''.join(tmp)
		
		
if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	print sol.convert("PAYPALISHIRING", 3)