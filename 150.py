class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numStack = []
        for n in tokens:
            if n in ["+", "-", "*", "/"]:
                b = numStack.pop()
                a = numStack.pop()
                r = 0
                if n == "+":
                    r = a + b
                elif n == "-":
                    r = a - b
                elif n == "*":
                    r = a * b
                elif n == "/":
                    r = 1.0 * a / b
                numStack.append(int(r))
            else:
                numStack.append(int(n))
        return numStack[0]
