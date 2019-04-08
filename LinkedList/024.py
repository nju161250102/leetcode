def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    headNode = ListNode(None)
    headNode.next = head
    cur = headNode
    while cur.next and cur.next.next:
        p = cur.next.next
        # �������
        cur.next.next = p.next
        p.next = cur.next
        cur.next = p
        # �����һ��Ľ���
        cur = p.next
    return headNode.next