from bisect import bisect_left

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):
		res = []
		num = sorted(num)
		for idx1, val in enumerate(num):
			val1 = val
			for idx2 in range( idx1+1, len(num) ):
				val2 = num[idx2]
				target = -(val1+val2)
				if target < val2:
					continue
				targetIdx = self.binarysearch(num, target, idx2+1, len(num) )
				if targetIdx >= 0 and  [val1, val2, target] not in res:
					res.append( [val1, val2, target] )
		return res
		
	def binarysearch(self, a, x, lo, hi):
		pos = bisect_left(a, x, lo, hi)
		return pos if pos != hi and a[pos] == x else -1 

if __name__ == "__main__":
	sol = Solution()
	# print sol.threeSum([1, 2, -3, 4, 5])
	print sol.threeSum([-1,0, 1, 2, -1, -4])