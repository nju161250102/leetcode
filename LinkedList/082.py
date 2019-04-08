def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return
    headNode = ListNode(None)
    headNode.next = head
    pre = headNode
    cur = head
    while cur:
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        if cur == pre.next:
            pre = pre.next
        else:
            pre.next = cur.next
        cur = cur.next
    return headNode.next
