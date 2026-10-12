class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_water = 0
        while left < right:
            width = right-left
            cur_water = width * min(heights[right],heights[left])

            if cur_water > max_water:
                max_water = cur_water

            if heights[left] > heights[right]:
                right-=1
            
            else:
                left+=1

        return max_water

        