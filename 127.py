class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        if not endWord in word_set:
            return 0
        else:
            word_set.remove(endWord)
        
        q1 = set([beginWord])
        q2 = set([endWord])
        temp = set([])
        count = 0
        
        while len(q1) != 0 and len(q2) != 0:
            count += 1
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            temp = set([])
            
            for word in q1:
                w_list = list(word)
                for i in range(len(w_list)):
                    hold = w_list[i]
                    for c in string.ascii_lowercase[:26]:
                        w_list[i] = c
                        w = ''.join(w_list)
                        if w in q2:
                            return count + 1
                        if w in word_set:
                            word_set.remove(w)
                            temp.add(w)
                    w_list[i] = hold
            q1 = temp
        return 0