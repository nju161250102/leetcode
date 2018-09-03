class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        num_dict = {}
        for num in candidates:
            if num_dict.has_key(num):
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        num_keys = num_dict.keys()
        def fun(array, d, pos):
            array_sum = sum(array)
            if (array_sum > target):
                return
            elif (array_sum == target):
                result.append(array)
                return
            for i in range(pos, len(num_keys)):
                array_sum = sum(array)
                new_array = array[:]
                new_array.append(num_keys[i])
                new_dict = d.copy()
                new_dict[num_keys[i]] -= 1
                next_pos = i+1 if new_dict[num_keys[i]] == 0 else i
                fun(new_array, new_dict, next_pos)
        
        fun([], num_dict, 0)
        return result