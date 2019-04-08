def sortedListToBST(self, head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    self.arr = []
    while head:
        self.arr.append(head.val)
        head = head.next
    return self.toBST(0, len(self.arr))

def toBST(self, l, r):
    if l >= r:
        return None
    mid = (l+r)/2
    root = TreeNode(self.arr[mid])
    root.left = self.toBST(l, mid)
    root.right = self.toBST(mid+1, r)
    return root