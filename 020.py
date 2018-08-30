class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if len(stack) == 0: return False
                end = stack[-1]
                if (end == '(' and c == ')') or (end == '[' and c == ']') or (end == '{' and c == '}'):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0