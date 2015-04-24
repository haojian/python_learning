# rotation to left or to right
# how to determine the rotation?
# check the increasing part for binary search


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def binarysearch(self, A, target):
		li = 0
		ri = len(A)-1
		while(li <= ri):
			mi = (li+ri)/2
			if A[mi] == target:
				return mi
			if mi == li:
				return -1
			if target > A[mi]:
				li = mi+1
			else:
				ri = mi-1
		return -1
			
	
if __name__ == "__main__":
	a = range(100)
	sol = Solution()
	print sol.binarysearch(a, 65)
