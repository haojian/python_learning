class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
		if n<0:
			return 1/self.myPow(x, -n)
		if n==0:
			return 1
		if n==1:
			return x
		if n==2:
			return x*x
		tmp = self.myPow(x, n/2)
		if n%2 == 1:
			return tmp*tmp*x
		else:
			return tmp*tmp