class Solution:
    ## 基于比较的排序算法，时复下限为 0(nlogn), 更优的方法是使用计数排序

    # 计数排序 时复为 O（n）
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ans = [0] * (n+1)
        for i in  citations:
            ans[min(i, n)] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += ans[i]
            if total >= i:
                return i



    

    # 方式1: 倒序遍历 需要完整遍历 数组才能找到符合的最大值
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        max_ = 0 # 要求 h 最大， 也就是 符合要求的 i 最大
        for i, j in enumerate(citations, 1):
            if j >= i:
                max_ = max(max_, i)

        return max_
    
    # 方式2 : 正序遍历 ： 找到的第一个可行解就是答案
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        n = len(citations)   

        for i, j in zip(range(n, 0, -1), citations):
            if j >= i:
                return i
        
        return 0
