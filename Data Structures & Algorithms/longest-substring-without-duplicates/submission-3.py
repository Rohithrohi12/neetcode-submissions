class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        sets = set()
        cur_len = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in sets:
                sets.remove(s[left])
                left+=1
            sets.add(s[right])
            cur_len = right-left+1
            if cur_len > max_len:
                max_len = cur_len
        return max_len
        
        