class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for i in s:
            if i.isalnum():
                new_string+=i
        if new_string.lower()==new_string[::-1].lower():
            return True
        return False
        

        