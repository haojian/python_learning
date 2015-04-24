class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
		bits = [0] * 32
		counterNeg = 0
		for x in A:
			if x < 0:
				counterNeg += 1
				x = -x
			curbits = bin(x)[2:][::-1]
			for idx, bit in enumerate(curbits):
				bits[idx] += int(bit)
		res = 0
		sign = 1 if counterNeg%3 == 0 else -1
		for idx, bit in enumerate(bits):
			res += 1 * ((bit%3) << idx)
		return res * sign
		
if __name__ == "__main__":
	sol = Solution()
	print sol.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
	print sol.singleNumber([2,2,1,1,3,1,3,3,4,2])
	print sol.singleNumber([2,2,2,3])
	print sol.singleNumber([43,16,45,89,45,-2147483648,45,2147483646,-2147483647,-2147483648,43,2147483647,-2147483646,-2147483648,89,-2147483646,89,-2147483646,-2147483647,2147483646,-2147483647,16,16,2147483646,43])
	
		