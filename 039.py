class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        def fun(array, pos):
            for i in range(pos, len(candidates)):
                array_sum = sum(array)
                if (array_sum > target):
                    break
                elif (array_sum == target):
                    result.append(array)
                    break
                else:
                    new_array = array[:]
                    new_array.append(candidates[i])
                    fun(new_array, i)
        
        fun([], 0)
        return result