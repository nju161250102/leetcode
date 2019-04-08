def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    length = 0
    headNode = ListNode(None)
    headNode.next = head
    p = q = headNode  # 双指针

    # 首先获取长度
    while p.next is not None:
        length += 1
        p = p.next
    if k % length == 0:
        return head
    # 到达应当作为末尾的结点
    for i in range(length - k % length):
        q = q.next
    # 修改链表指针顺序
    p.next = headNode.next
    headNode.next = q.next
    q.next = None
    return headNode.next
