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
        # 如果到达结尾则转到另一个的开头
        # 在第二轮相遇处即为结果（如果没有重合结点则恰巧都到尾部，为None）
        a = a.next if a else headB
        b = b.next if b else headA
    return a

    # 方法二：使用集合保存已有的结点
    # s = set()
    # while headA:
    #     s.add(headA)
    #     headA = headA.next
    # while headB:
    #     if headB in s:
    #         return headB
    #     headB = headB.next
    # return None