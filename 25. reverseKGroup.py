# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
	def reverseKGroup(self, head, k):
		if k == 1: 
			return head
		preHeader = ListNode(0)
		preHeader.next = head
		left = preHeader
		nodes = [0] * (k+2)
		while self.ifReverse(left, k, nodes):
			nodes[0].next = nodes[k]
			for offset in range(k-1):
				nodes[k-offset].next = nodes[k-offset-1]
			nodes[1].next = nodes[k+1]
			left = nodes[1]
		return preHeader.next

	def ifReverse(self, prenode, k, nodes):
		curNode = prenode
		for i in range(k+1):
			if curNode:
				nodes[i] = curNode
				curNode = curNode.next
			else:
				return False
		nodes[k+1] = curNode
		return True