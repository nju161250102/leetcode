# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        p = head
        copyHead = None
        copy = None
        nodeList = []
        randomList = []
        copyList = []
        while p is not None:
            newNode = RandomListNode(p.label)
            if len(copyList) > 0:
                copyList[-1].next = newNode
            if copyHead is None:
                copyHead = newNode
            copyList.append(newNode)
            nodeList.append(p)
            randomList.append(p.random)
            p = p.next
        
        for i, node in enumerate(randomList):
            if node is not None:
                nodeIndex = nodeList.index(node)
                copyList[i].random = copyList[nodeIndex]
        return copyHead
                