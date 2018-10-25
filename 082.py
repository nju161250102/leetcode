# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        p = head
        q = head
        new_head = None
        new_p = None
        
        while p is not None:
            if p.next is not None and p.next.val == p.val:
                q = None
            else:
                if q is not None:
                    print q.val
                    if new_head is None:
                        new_head = q
                        new_p = q
                    else:
                        new_p.next = q
                        new_p = new_p.next
                q = p.next
            p = p.next
        
        if new_p is not None:
            new_p.next = None
        return new_head
