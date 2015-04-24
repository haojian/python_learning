# rotation to left or to right
# how to determine the rotation?
# check the increasing part for binary search


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
		li = 0
		ri = len(A)-1
		while li <= ri:
			mi = (li+ri)/2
			if A[mi] == target:
				return mi
			if A[li] <= A[mi]:
				if A[li] <= target < A[mi]:
					ri = mi-1
				else:
					 li = mi+1
			elif A[mi] <= A[ri]:
				if A[mi] < target <= A[ri]:
					li = mi+1
				else:
					ri = mi-1
		return -1
			
if __name__ == "__main__":
	a = range(6, 10) + range(5)
	print a
	sol = Solution()
	print sol.search(a, 3)
	print sol.search([1], 1)
	print sol.search([1,3], 3)
	print sol.search([1], 0)