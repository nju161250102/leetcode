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
        
        while p.next is not None:
            q = p.next
            if p.val == q.val:
                p.next = q.next
            else:
                p = q
            
        return head
      