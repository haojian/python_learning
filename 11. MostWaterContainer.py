class Solution:
    # @return an integer
    def maxArea(self, height):
		maxarea = 0
		left = 0
		right = len(height) - 1
		while left < right:
			newarea = (right - left) * min(height[left], height[right])
			maxarea = max(newarea, maxarea)
			if height[left] < height[right]:
				left += 1
			else:
				right -= 1
		return maxarea
		
if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	print sol.maxArea([1, 2, 3, 4, 5])
