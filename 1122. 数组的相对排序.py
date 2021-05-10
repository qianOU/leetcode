class Solution:
    # 基于优先队列
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from queue import PriorityQueue as pq
        map_ = {i:j for j,i in enumerate(arr2)}
        
        p = pq()
        appear = []
        for i in arr1:
            if i in map_.keys():
                p.put((map_[i], i))
            else:
                appear.append(i)
        
        ans = []
        while not p.empty():
            ans.append(p.get())
        
        ans.entend(sorted(appear))

        return ans
    
    # 方法2： 基于特殊的自定义比较函数即可
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def mycomp(x):
            return (0, rank[x]) if x in rank else (1, x)

        rank = {i:j for j,i in enumerate(arr2)}

        return sorted(arr1, key=mycomp)
