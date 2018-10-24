# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p = None
        q = head
        i = 1
        while i < m:
            p = q
            q = q.next
            i += 1
            
        a = p
        b = q
        
        while i < n+1:
            m = q.next
            q.next = p
            p = q
            q = m
            i += 1
        
        b.next = q
        if a is None:
            return p
        else:
            a.next = p
        
        return head
