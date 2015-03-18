# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
		preHeader = ListNode(0)
		node1 = l1
		node2 = l2
		curNode = preHeader
		while node1 and node2:
			if node1.val < node2.val:
				curNode.next = node1
				node1 = node1.next
			else:
				curNode.next = node2
				node2 = node2.next
			curNode = curNode.next
		if node1:
			curNode.next = node1
		if node2:
			curNode.next = node2
		return preHeader.next

