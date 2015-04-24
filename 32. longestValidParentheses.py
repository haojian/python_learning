class Solution:
    # @param s, a string
    # @return an integer

#use the dp to record the length of longest substring end with that position
#multiple cases:
# ()()
# if s[k] = ):
# 	if  s[k-1] = (:
#		dp[k] = 2 + dp[k-2] (if exist)
#	if	dp[idx-1]!=0 and s[k-1] = ):
#		otherside = idx-1-dp[idx-1]
#		if s[otherside] == '(':
#			dp[k] = 2 + dp[idx-1] + dp[otherside-1] (if exist)
#		else:
#			dp[k] = 0
#	elif s[k-1] == ):
#		dp[k] = 0

	def longestValidParentheses(self, s):
		if len(s) == 0:
			return 0
		dp = [0] * len(s) 
		for idx, char in enumerate(s):
			if char == ')':
				if idx == 0:
					continue
				if s[idx-1] == '(':
					dp[idx] = 2 + (dp[idx-2] if idx >=2 else 0)
				elif s[idx-1] == ')' and dp[idx-1] != 0:
					#check if match
					otherside = idx-1-dp[idx-1]
					if otherside >= 0 and s[otherside] == '(':
						dp[idx] = 2 + dp[idx-1] + (dp[otherside-1] if otherside >=1 else 0)
		return max(dp)
		
if __name__ == "__main__":
	sol = Solution()
	print sol.longestValidParentheses("(()))())(")