# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
		if n == 0:
			return head
		preHeader = ListNode(0)
		preHeader.next = head
		leftHeader = preHeader
		rightHeader = leftHeader
		while n >= 0:
			rightHeader = rightHeader.next
			n -= 1
		while rightHeader:
			rightHeader = rightHeader.next
			leftHeader = leftHeader.next
		leftHeader.next = leftHeader.next.next
		return preHeader.next
		
if __name__ == "__main__":
	sol = Solution()
	nodea = ListNode(1)
	print sol.removeNthFromEnd(nodea, 1)