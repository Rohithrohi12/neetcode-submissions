class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        new_list = []
        for i in range(len(nums)-1):
            left = i+1
            right = len(nums)-1
            while left < right:
                summed = nums[i]+nums[left]+nums[right]

                if summed==0:
                    if [nums[i],nums[left],nums[right]] not in new_list:
                        new_list.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif summed > 0:
                    right-=1
                elif summed<0:
                    left+=1
        return new_list
        