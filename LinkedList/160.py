def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if headA is None or headB is None:
        return None
    a = headA
    b = headB
    while a is not b:
        # ��������β��ת����һ���Ŀ�ͷ
        # �ڵڶ�����������Ϊ��������û���غϽ����ǡ�ɶ���β����ΪNone��
        a = a.next if a else headB
        b = b.next if b else headA
    return a

    # ��������ʹ�ü��ϱ������еĽ��
    # s = set()
    # while headA:
    #     s.add(headA)
    #     headA = headA.next
    # while headB:
    #     if headB in s:
    #         return headB
    #     headB = headB.next
    # return None