# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
		preHeader = ListNode(0)
		cur = preHeader
		carry = 0
		while l1 and l2:
			tmp = l1.val + l2.val + carry
			carry = tmp / 10
			cur.next = ListNode( tmp - carry*10 )
			l1 = l1.next
			l2 = l2.next
			cur = cur.next
		while l1:
			tmp = l1.val + carry
			carry = tmp / 10
			cur.next = ListNode( tmp - carry*10 )
			l1 = l1.next
			cur = cur.next
		while l2:
			tmp = l2.val + carry
			carry = tmp / 10
			cur.next = ListNode( tmp - carry*10 )
			l2 = l2.next
			cur = cur.next
		if carry > 0:
			cur.next = ListNode(carry)
		return preHeader.next