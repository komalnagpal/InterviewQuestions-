# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        dummy_node.next = head
        current = dummy_node
        while(current.next is not None and current.next.next is not None):
            first_node = current.next
            second_node = current.next.next
            first_node.next = second_node.next
            current.next = second_node
            current.next.next = first_node
            current = current.next.next
        return dummy_node.next
