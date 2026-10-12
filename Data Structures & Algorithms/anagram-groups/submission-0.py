class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        new_list = []
        for index,value in enumerate(strs):
            key = "".join(sorted(value))
            if key not in seen:
                seen[key]=[]
            seen[key].append(strs[index])

        for i in seen.values():
            new_list.append(i)
        return new_list

            

        