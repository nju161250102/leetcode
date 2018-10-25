# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        l_head = None
        r_head = None
        l_p = None
        r_p = None
        p = head
        
        while p is not None:
            if p.val < x:
                if l_head is None:
                    l_p = ListNode(p.val)
                    l_head = l_p
                else:
                    l_p.next = ListNode(p.val)
                    l_p = l_p.next
            else:
                if r_head is None:
                    r_p = ListNode(p.val)
                    r_head = r_p
                else:
                    r_p.next = ListNode(p.val)
                    r_p = r_p.next
            p = p.next
        
        if l_head is None:
            return r_head
        if r_head is not None:
            l_p.next = r_head
        return l_head