class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
		num1 = num1[::-1]
		num2 = num2[::-1]
		res = []
		for idx1, char1 in enumerate(num1):
			for idx2, char2 in enumerate(num2):
				x1 = int(num1[idx1]) 
				x2 = int(num2[idx2])
				tmp = x1*x2
				if len(res) <= idx1+idx2:
					res.append(0)
				res[idx1+idx2] += tmp
		update = 0
		print res
		for idx, num in enumerate(res):
			res[idx] += update
			update = 0
			if res[idx] >= 10:
				update = res[idx]/10
				res[idx] %= 10
		if update != 0:
			res.append(update)
		res = res[::-1]
		resStr =  "".join(str(x) for x in res).lstrip("0")
		if len(resStr) == 0:
			resStr = "0"
		return resStr



if __name__ == "__main__":
	sol = Solution()
	print sol.multiply("39219", "6")