class Solution:
    #思路1: 先写个忽略有序条件的版本。基于值的二分
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, max(citations)

        while l <= r:
            mid = (l + r) // 2
            count = sum(i>=mid for i in citations)
            if mid <= count:
                l = mid + 1
            else:
                r = mid - 1
        
        return r
    
    # 思路2 : 使用 有序条件 0(log((v)log(n)))  V 是极差
    # 没有完全领悟题意呀
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, citations[-1]
        while l <= r:
            h = (l + r) // 2
            # 在有序列表中，找到第一个 大于等于 h 的索引
            l1, r1 = 0, n-1
            while l1 <= r1:
                mid = (l1 + r1) // 2
                if citations[mid] >= h:
                    r1 = mid - 1
                else:
                    l1 = mid + 1

            if n - l1 >= h:
                l = h + 1
            else:
                r = h - 1

        return r
    
    # 思路3: 时间上之需要找到第一个 citations[i] >= n-i 的位置，n-i 即是 h 的定义
    # 其实值得注意的是，如果找到了 citations[i] == n-i  则 i 的左侧不可能还有 满足  citations[i] >= n-i的索引存在
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n-1
        # 找寻的是左边界
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
        
        return n - l