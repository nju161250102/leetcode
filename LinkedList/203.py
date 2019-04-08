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
        # ��ͬ����¶�forwardָ��Ĵ���
        if front.val == val:
            forward.next = front.next
        else:
            forward = forward.next
        front = front.next
    return headNode.next