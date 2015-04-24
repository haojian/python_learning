class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
	def swapPairs(self, head):
		preHead = ListNode(0)
		preHead.next = head
		left = preHead
		while left and left.next and left.next.next:
			A = left
			B = left.next
			C = B.next
			D = C.next
			A.next = C
			C.next = B
			B.next = D
			left = B
		return preHead.next