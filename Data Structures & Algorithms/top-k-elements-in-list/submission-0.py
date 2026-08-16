class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}

        for num in nums:            
            seen[num]= seen.get(num, 0) + 1 

        order = sorted(seen.keys(), key = lambda x:seen[x], reverse=True)

        return order[:k]







        