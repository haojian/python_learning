from bisect import bisect_left

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
		num = sorted(num)
		res = []
		for idx1, val1 in enumerate(num):
			for idx2 in range(idx1+1, len(num)-2 ):
				map_val = {}
				for idx in range( idx2+1, len(num) ):
					lookup_val = target - num[idx1] - num[idx2] - num[idx]
					if map_val.has_key( num[idx] ):
						idx3 = map_val[ num[idx] ]
						idx4 = idx
						tmp = [ num[idx1], num[idx2], num[idx3], num[idx4] ]
						if tmp not in res:
							res.append( tmp )
					else:
						map_val[ lookup_val ] = idx
		return res			
	

if __name__ == "__main__":
	sol = Solution()
	print sol.fourSum([1, 0, -1, 0, -2, 2], 0)