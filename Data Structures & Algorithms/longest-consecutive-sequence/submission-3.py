class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new_list = sorted(set(nums))

        current_length = 1
        longest_length = 1

        for i in range(1, len(new_list)):
            if new_list[i] == new_list[i - 1] + 1:
                current_length += 1
            else:
                current_length = 1

            if current_length > longest_length:
                longest_length = current_length

        return longest_length
        