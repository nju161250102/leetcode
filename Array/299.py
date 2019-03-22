def getHint(self, secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    a = 0
    b = 0
    s_nums = collections.defaultdict(lambda: 0)  # 默认值是0
    g_nums = collections.defaultdict(lambda: 0)
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            a += 1
        s_nums[secret[i]] += 1
        g_nums[guess[i]] += 1
    for i in g_nums:
        b += min(s_nums[i], g_nums[i])
    return "%dA%dB" % (a, b-a)
