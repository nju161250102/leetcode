def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # 使用空的头结点
    head = ListNode(0)
    cur = head
    while l1 and l2:
        # 谁的值小就先连接谁，并将指针指向下一个节点
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    # 此时一条链已经为空，将剩余链直接拼接即可
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2
    return head.next
