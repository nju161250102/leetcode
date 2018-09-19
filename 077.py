class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        def fun(n, k, array):
            if k == len(array):
                result.append(array)
                return
            begin = 1 if len(array) == 0 else array[-1]+1
            for num in range(begin, n+1):
                new_array = array[:]
                new_array.append(num)
                fun(n, k, new_array)
        
        fun(n, k, [])
        return result
   