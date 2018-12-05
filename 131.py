class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.result = []
        
        def fun(string, partition):
            if string == "":
                self.result.append(partition)
                return
            for i in range(len(string)):
                flag = True
                for j in range((i+1)/2):
                    if string[j] != string[i-j]:
                        flag = False
                if flag:
                    new_partition = partition[:]
                    new_partition.append(string[:i+1])
                    fun(string[i+1:], new_partition)
        
        fun(s, [])
        return self.result