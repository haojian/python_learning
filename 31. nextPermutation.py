class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.

	#pseudo code
	#find the increasing pair and swap it
	#which pair? the swap should happen at the lower digit, the lower the better
	#happen means the left digit
	def nextPermutation(self, num):
		for li in range(len(num)-2, -1, -1):
			for ri in range(len(num)-1, li, -1):
				if num[ri] > num[li]:
					#swap ri and li
					print num[ri], num[li]
					tmp = num[ri] 
					num[ri] = num[li]
					num[li] = tmp
					num[li+1:] = sorted(num[li+1:])
					return
		else:
			num.reverse()	
			
if __name__ == "__main__":
	sol = Solution()
	num = [4,2,0,2,3,2,0]
	sol.nextPermutation(num)
	print num