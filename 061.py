# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        length = 1
        p = head
        while p.next is not None:
            length += 1
            p = p.next
        k = k % length
        if k == 0:
            return head
        p.next = head
        q = head
        while k < length - 1:
            q = q.next
            k += 1
        re = q.next
        q.next = None
        return re
