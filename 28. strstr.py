class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
		for idx in range(len(haystack)-len(needle)+1):
			for needle_idx in range(len(needle)):
				if haystack[idx+needle_idx] != needle[needle_idx]:
					break
			else:
				return idx
		else:
			return -1
			

if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	print sol.strStr("abc", "bc")