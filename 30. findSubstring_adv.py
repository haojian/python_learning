#########
# be careful there can have duplications in L.
#########

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integers
	def findSubstring(self, S, L):
		if len(L) == 0 or len(L[0]) == 0:
			return []
		len_pattern = len(L[0])
		map_list = {}
		res = []
		for idx, val in enumerate(L):
			if val in map_list:
				map_list[val] = map_list[val]+1
			else:
				map_list[val] = 1
			
		for idx in range(len(S)):
			cache = {}
			for p_idx in range(len(L)):
				if (idx+(p_idx+1)*len_pattern) > len(S):
					break
				try:
					mapped_idx = L.index(S[idx+p_idx*len_pattern:idx+(p_idx+1)*len_pattern])
					if L[mapped_idx] in cache:
						cache[L[mapped_idx]] = cache[L[mapped_idx]]+1
					else:
						cache[L[mapped_idx]] = 1
					if cache[L[mapped_idx]] > map_list[L[mapped_idx]]:
						break
				except:
					break
			shared_items = set(cache.items()) & set(map_list.items())
			if len(shared_items) == len(map_list):
				res.append(idx)
		return res
		
		
if __name__ == "__main__":
	sol = Solution()
	print sol.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])