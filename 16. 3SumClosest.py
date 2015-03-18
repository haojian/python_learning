from bisect import bisect_left
import sys

class Solution:
    # @return an integer
	def threeSumClosest(self, num, target):
		closestTarget = sys.maxint
		num = sorted(num)
		for idx1, val in enumerate(num):
			val1 = val
			for idx2 in range(idx1+1, len(num)-1):
				val2 = num[idx2]
				lookupval = target-val1-val2
				pos = bisect_left(num, lookupval, idx2+1, len(num))
				if pos == len(num):
					val3 = num[pos-1]
				elif pos == idx2+1:
					val3 = num[pos]
				else:
					val3 = num[pos-1] if abs(num[pos-1]-lookupval) < abs(num[pos]-lookupval) else num[pos]
				if abs(val1+val2+val3-target) < abs(closestTarget-target):
					closestTarget = val1+val2+val3
		return closestTarget
		
if __name__ == "__main__":
	sol = Solution()
	print sol.threeSumClosest([-1, 2, 1, -4], 1)
