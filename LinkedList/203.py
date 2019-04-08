def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    headNode = ListNode(None)
    headNode.next = head
    forward = headNode
    front = headNode.next
    while front:
        # 不同情况下对forward指针的处理
        if front.val == val:
            forward.next = front.next
        else:
            forward = forward.next
        front = front.next
    return headNode.next