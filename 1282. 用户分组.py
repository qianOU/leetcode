class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import defaultdict
        dic = defaultdict(list)
        ans = []
        for i, j in enumerate(groupSizes):
            if len(dic[j]) == j:
                ans.append(dic[j].copy())
                dic[j].clear() 
            dic[j].append(i)
        
        for j in dic:
            if dic[j]:
                ans.append(dic[j])
        
        return ans
