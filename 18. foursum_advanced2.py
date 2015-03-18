from bisect import bisect_left

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
	def fourSum(self, num, target):
		num = sorted(num)
		pairs = []
		for idx1 in range(len(num)-1):
			for idx2 in range(idx1+1, len(num)):
				pairs.append( [idx1, idx2] )
		res = []
		map_val = {}
		for idx, pair in enumerate(pairs):
			sum1 = num[ pair[0] ] + num[ pair[1] ]
			lookup_val = target - sum1
			if map_val.has_key(lookup_val):
				pair1 = pair
				for pair2_idx in map_val[lookup_val]:
					pair2 = pairs[ pair2_idx ]
					merged= self.mergePair(pair1, pair2)
					if merged:
						orig = [num[x] for x in merged]
						if orig not in res:
							res.append(orig)
			if sum1 in map_val:
				map_val[sum1].append(idx)
			else:
				map_val[sum1] = [idx]
		return res
		
	def mergePair(self, pair1, pair2):
		res = set(pair1) | set(pair2)
		if len(res) != 4:
			return
		return sorted(list(res))			


if __name__ == "__main__":
	sol = Solution()
	print sol.fourSum([0,2,2,2,10,-3,-9,2,-10,-4,-9,-2,2,8,7], 6)