class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            diff_val = target-num
            
            if diff_val in seen:
                return[seen[diff_val],i]
            seen[num]=i
            

        