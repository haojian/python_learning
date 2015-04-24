class Solution:
    # @return an integer
	def divide(self, dividend, divisor):
		sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
		dividend = abs(dividend)
		divisor = abs(divisor)
		
		tmp_divisor = divisor
		res = 0
		while dividend >= divisor:
			k = 0
			tmp_divisor = divisor << 1
			while dividend >= tmp_divisor:
				tmp_divisor <<= 1
				k += 1
			tmp_divisor >>= 1
			dividend -= tmp_divisor
			res += 1 << k
		res = res * sign
		# if res > MAX_INT:
		# 	return MAX_INT
		return min(max(-2147483648, res), 2147483647)  
		
if __name__ == "__main__":
	sol = Solution()
	print sol.divide(100, 1)
	print sol.divide(100, 6)