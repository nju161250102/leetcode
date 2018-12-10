class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        delta = [gas[i] - cost[i] for i in range(len(gas))]
        
        first = None
        leftSum = 0
        s = 0
        for i in xrange(len(delta)):
            if delta[i] >= 0 and s <= 0:
                first = i
                leftSum += s
                s = delta[i]
            else:
                s += delta[i]
        if first is not None and s + leftSum >= 0:
            return first
        else:
            return -1