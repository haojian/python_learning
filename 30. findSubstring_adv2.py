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
		counter = {}
		for val in L:
			if val in counter:
				counter[val] += 1
			else:
				counter[val] = 1
		res = []
		totallen =  len(L[0]) * len(L)
		for p_idx in range(len_pattern):
			cache = dict(counter)
			li = 0
			while(p_idx + li*len_pattern +totallen) <= len(S):
				for offset in range(len(L)):
					tmp = S[p_idx + (li+offset)*len_pattern:p_idx + (li+offset+1)*len_pattern]
					if tmp in cache:
						cache[tmp] -= 1
						if self.checkifMatched(cache):
							res.append( p_idx + li*len_pattern )
							li += 1
							cache = dict(counter)
							break
						elif cache[tmp] < 0:
							li += 1
							cache = dict(counter)
							break
					else:
						li += 1
						cache = dict(counter)
						break
				else:
					li += 1
					cache = dict(counter)
		return res
						
			
	def checkifMatched(self, cache):
		for key, val in cache.items():
			if val != 0:
				return False
		else:
			return True
		
		

		
		
if __name__ == "__main__":
	sol = Solution()
	print sol.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
	print sol.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])