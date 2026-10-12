class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for i in s:
            d1[i] = d1.get(i,0)+1
        for i in t:
            d2[i] = d2.get(i,0)+1
        for key,value in d1.items():
            if key in d2.keys():
                if d1[key]!=d2[key]:
                    return False
            else:
                return False
        for key,value in d2.items():
            if key in d1.keys():
                if d1[key]!=d2[key]:
                    return False
            else:
                return False
        return True

        
        