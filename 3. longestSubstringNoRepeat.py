class Solution:
	# @return a tuple, (index1, index2)
	def lengthOfLongestSubstring(self, s):
		start_idx	= 0
		char_map	= {}
		tmp_length	= 0
		max_length	= 0
		for idx, char in enumerate(s):
			if char not in char_map:
				tmp_length	+= 1
			else:
				start_idx	= start_idx if start_idx > char_map[char] else char_map[char] + 1
				tmp_length	= (idx - start_idx) + 1
			char_map[char]	= idx
			if tmp_length > max_length:
				max_length = tmp_length
		return max_length
			
if __name__ == "__main__":  
	# print __name__
	sol = Solution()
	print sol.lengthOfLongestSubstring("ssssss")
	print sol.lengthOfLongestSubstring("abba")
	print sol.lengthOfLongestSubstring("uqinntq")
