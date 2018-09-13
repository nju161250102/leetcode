# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        put_flag = False
        for i, interval in enumerate(intervals):
            if interval.start > newInterval.end or interval.end < newInterval.start:
                if interval.start > newInterval.start and not put_flag:
                    result.append(newInterval)
                    put_flag = True
                result.append(interval)
            else:    
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)
                if not put_flag:
                    result.append(newInterval)
                    put_flag = True
                else:
                    result[-1] = newInterval
        if not put_flag:
            result.append(newInterval)
        return result
        