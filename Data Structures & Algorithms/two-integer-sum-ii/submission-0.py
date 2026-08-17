class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        total = {}
        ret = [] 

        for i in range(len(numbers)):
            temp = target - numbers[i]

            if temp in total: 
                return [total[temp] + 1, i + 1 ]
                

            total[numbers[i]] = i 

        return ret 
        