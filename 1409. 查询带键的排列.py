class Solution:
    def processQueries(self, queries, m: int) :
        index = list(i-1 for i in range(1, m+1))

        # from sortedcontainers import SortedList
        # a = SortedList()
        # for i in range(m):
        #     a.add(i+1)
        a = list(range(1, m+1))
        
        ans = []
        for i in queries:
            idx = i-1
            ans.append(index[idx])
            
            for j in range(m):
                if index[j] < index[idx] and j!=idx:
                    index[j] += 1
            
            index[idx] = 0
            # print(i, idx,  index)
        return ans

        
        
        


print(Solution().processQueries(
[8,7,4,2,8,1,7,7],
8
))    
        
        