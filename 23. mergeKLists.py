from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
		h = []
		preHeader = ListNode(0)
		cur = preHeader
		for idx, nodek in enumerate(lists):
			if nodek:
				heappush(h, (nodek.val, idx, nodek))
		while len(h) > 1:
			smallest = heappop(h)
			if smallest[2].next:
				nodek = smallest[2].next
				heappush(h, (nodek.val, idx, nodek))
			cur.next = smallest[2]
			cur = cur.next
		if len(h) != 0:
			cur.next = heappop(h)[2]
		return preHeader.next
		
		