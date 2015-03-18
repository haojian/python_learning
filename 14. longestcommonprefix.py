class Solution:
	# @return a string
	def longestCommonPrefix(self, strs):
		if len(strs) == 0:
			return ''
		if len(strs) == 1:
			return strs[0]
		if len(strs) == 2:
			return self.getCommonPrefix(strs[0], strs[1])
		left = strs[:len(strs)/2]
		right = strs[len(strs)/2:]
		return self.getCommonPrefix( self.longestCommonPrefix(left), self.longestCommonPrefix(right) )
			
	def getCommonPrefix(self, str1, str2):
		res = ''
		for char1, char2 in zip(str1, str2):
			if char1 == char2:
				res += char1
			else:
				break
		return res

if __name__ == "__main__":
	sol = Solution()
	print sol.longestCommonPrefix(["a", "a", "b"])