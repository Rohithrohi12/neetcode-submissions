class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index,value in enumerate(numbers):
            diff_val = target-value

            if diff_val in seen:
                return [seen[diff_val]+1,index+1]

            seen[value]= index

        return []

        