def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    d = {u'(': u')', u'[': u']', u'{': u'}'}
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if len(stack) == 0: return False
            end = stack.pop()
            if c != d[end]:
                return False
    return len(stack) == 0