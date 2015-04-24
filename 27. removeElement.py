class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        lastidx = 0
        for i in range(0, len(A) ):
            if A[i] == elem:
                continue
            else:
                A[lastidx] = A[i]
                lastidx += 1
        return lastidx