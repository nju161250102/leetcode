class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        
        def dfs(a):
            if len(a) == 4:
                if 0 <= int(a[-1]) <= 255:
                    if len(a[-1]) > 1 and a[-1][0] == '0':
                        return
                    result.append(".".join(a))
                return
            num_str = a[-1]
            for i in range(1, min(4, len(num_str))):
                if i > 1 and num_str[0] == '0':
                    continue
                new_num = int(num_str[0:i])
                if 0 <= new_num <= 255:
                    a[-1] = num_str[0:i]
                    a.append(num_str[i:])
                    dfs(a)
                    del(a[-1])
                    a[-1] = num_str
            return
        
        dfs([s])
        return result
