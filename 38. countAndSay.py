class Solution:
    # @return a string
	def countAndSay(self, n):
		if n == 1:
			return "1"
		orig = self.countAndSay(n-1)
		return self.strToSaying(orig)
		
		
	def strToSaying(self, orig):
		if len(orig) == 0:
			return ""
		counter = 1
		curChar = orig[0]
		res = ""
		for idx in range(1, len(orig)):
			if orig[idx] == curChar:
				counter += 1
			else:
				res += str(counter) + str(curChar)
				curChar = orig[idx]
				counter = 1
		res += str(counter) + str(curChar)
		return res
		
		
if __name__ == "__main__":
	sol = Solution()
	print sol.countAndSay(2)
	print sol.countAndSay(3)
	print sol.countAndSay(10)
	print sol.countAndSay(11)