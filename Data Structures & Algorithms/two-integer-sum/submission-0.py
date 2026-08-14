class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []

        for i in range(len(nums)):
            temp = target - nums[i]

            if temp in seen:
                return [seen[temp], i]
                        ##indexTem: index of curr num 

            seen[nums[i]] = i   ## This is the seen[nums[i]] = i 
                                                ##   value   index of val

        '''
        1st Iter
        3 , 4 , 5, 6 

        temp = 7 - 3 == 4

        if 4 in seen(empty)
            skip
        seen[3] = 0  ----> dict = {'3': 0}

        2nd Iter 

        temp = 7 - 4 = 3
        if 3 in seen: only {'3': 0}

        yes so we return 
            return (seen[temp] // which was 0({'4': 0})  and i is 1 )

'''
   




