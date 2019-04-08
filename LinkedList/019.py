def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # ʹ�ö����ͷ�����⸴���ж�
    headNode = ListNode(0)
    headNode.next = head
    quick = slow = headNode  # ˫ָ��
    for _ in range(n+1):
        # ָ�����Ϊn+1
        quick = quick.next
    while quick:
        # ǰ���ָ�뵽ĩβʱ�����ָ��Ϊ��ɾ������ǰ���ڵ�
        quick = quick.next
        slow = slow.next
    slow.next = slow.next.next
    # ����ԭ�����׽ڵ�
    return headNode.next