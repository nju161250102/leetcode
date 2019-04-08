def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(None)
    p = head
    k = 0
    while l1 is not None or l2 is not None:
        if l1 and l2:
            s, k = self.add(l1.val, l2.val, k)
        else:
            # 只加不为None的链表
            s, k = self.add(0, (l1 or l2).val, k)
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        p.next = ListNode(s)
        p = p.next
    # 如果最后有进位，则再加上一个结点
    if k != 0:
        p.next = ListNode(k)
    return head.next 

def add(self, a, b, k):
    # 计算个位数和进位
    s = a + b + k
    if s >= 10:
        s = s - 10
        k = 1
    else:
        k = 0
    return s, k