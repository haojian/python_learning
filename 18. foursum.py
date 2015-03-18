from bisect import bisect_left

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
	def fourSum(self, num, target):
		num = sorted(num)
		res = []
		for idx1, val1 in enumerate(num):
			if num[idx1] > 0:
				continue
			for idx2 in range(idx1+1, len(num)-2 ):
				if num[idx1]+num[idx2] > 0:
					continue
				for idx3 in range(idx2+1, len(num)-1 ):
					targetVal = target-(num[idx1] + num[idx2] + num[idx3]) 
					if num[idx3+1] > targetVal:
						continue
					idx4 = self.binarySearch(num, targetVal, idx3+1, len(num) )
					if idx4 != -1:
						tmp = [ num[idx1], num[idx2], num[idx3], num[idx4] ]
						if tmp not in res:
							res.append( tmp )
		return res
					
	
	def binarySearch(self, a, x, low, high):
		pos = bisect_left(a, x, low, high)
		return pos if pos < high and a[pos] == x else -1
		
		
if __name__ == "__main__":
	sol = Solution()
	print sol.fourSum([1, 0, -1, 0, -2, 2], 0)