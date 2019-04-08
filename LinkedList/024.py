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
        # 链表操作
        cur.next.next = p.next
        p.next = cur.next
        cur.next = p
        # 完成了一组的交换
        cur = p.next
    return headNode.next