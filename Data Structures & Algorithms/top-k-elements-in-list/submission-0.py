class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        sorted_set = set()
        for i in nums:
            d[i]=d.get(i,0)+1
        d = sorted(d , key=d.get,reverse=True)
        
        for i in range(len(d)):
            if len(sorted_set) < k:
                sorted_set.add(d[i])
        return list(sorted_set)



        