class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            s_list = list(s)
            s_list.sort()
            sort_s = "".join(s_list)
            if d.has_key(sort_s):
                d[sort_s].append(s)
            else:
                d[sort_s] = [s]
        return d.values()
