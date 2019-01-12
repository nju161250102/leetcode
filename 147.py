# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        p = head.next
        while p is not None:
            preNode = None
            temp = p.next
            node = head
                
            insert = False
            while node != p:
                if p.val < node.val and not insert:
                    insert = True
                    p.next = node
                    if preNode is None:
                        head = p
                    else:
                        preNode.next = p
                preNode = node
                node = node.next
            p = temp
            if preNode is not None and insert:
                preNode.next = p
        
        return head
