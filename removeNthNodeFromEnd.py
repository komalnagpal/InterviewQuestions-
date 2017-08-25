# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head is None or (head.next is None and n ==1):
            return None
        start = ListNode(0)
        p1 = start
        p2 = start
        start.next = head
        for i in range(n+1):
            if p1 is None:
                return head
            p1 = p1.next
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return start.next
            
            
