def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # 使a的长度大于等于b
    if len(a) < len(b):
        a, b = b, a
    d = 0  # 进位
    re = ""  # 结果
    for i in range(len(a)):
        char_a = a[len(a) - i - 1]
        char_b = b[len(b) - i - 1] if i < len(b) else '0'
        s = int(char_a) + int(char_b) + d
        if s > 1:
            d = 1
            s -= 2
        else:
            d = 0
        re = str(s) + re
    # 如果最后还剩进位
    if d > 0:
        re = str(d) + re
    return re
