class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        str_list = [("", 0, 0)]
        while True:
            new_list = []
            for s in str_list:
                if s[1] < n:
                    new_str = (s[0]+'(', s[1]+1, s[2])
                    new_list.append(new_str)
                if s[2] < s[1]:
                    new_str = (s[0]+')', s[1], s[2]+1)
                    new_list.append(new_str)
            if len(new_list) == 0:
                break
            
            str_list = new_list
        return [x[0] for x in str_list]