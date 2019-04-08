def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # 使用额外的头结点避免复杂判断
    headNode = ListNode(0)
    headNode.next = head
    quick = slow = headNode  # 双指针
    for _ in range(n+1):
        # 指针间间距为n+1
        quick = quick.next
    while quick:
        # 前面的指针到末尾时后面的指针为待删除结点的前驱节点
        quick = quick.next
        slow = slow.next
    slow.next = slow.next.next
    # 返回原来的首节点
    return headNode.next