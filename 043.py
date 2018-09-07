class Solution(object):
    def unit(self, num):
        return num % 10
    
    def ten(self, num):
        return num / 10
    
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        mul_list = []
        m = len(num1)
        n = len(num2)
        
        pre = []
        result = ""
        add = 0
        for k in range(0, m+n-1):
            begin = 0 if k < m else k-m+1
            end = k if k < n else n-1
            mul_list = []
            mul_result = 0
            for i in range(begin, end+1):
                try:
                    mul = int(num1[-k+i-1]) * int(num2[-i-1])
                except:
                    mul = 0
                mul_list.append(mul)
                mul_result += self.unit(mul)
            for mul in pre:
                mul_result += self.ten(mul)
            mul_result += add
            result = str(self.unit(mul_result)) + result
            add = self.ten(mul_result)
            pre = mul_list
        if self.ten(pre[0]) + add != 0:
            result = str(self.ten(pre[0]) + add) + result
        return result