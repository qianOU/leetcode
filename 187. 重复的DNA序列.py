class Solution:
    # 滑动窗口 基于字符串的比较，耗时，适宜使用 hash 算法
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import deque
        n = len(s)
        if n <= 10: return []

        r = 10
        window = deque(s[:10])
        vis = set([''.join(window)])
        res = set()

        while r < n:
            window.popleft()
            window.append(s[r])
            item = ''.join(window)
            if item in vis:
                res.add(item)
            else: vis.add(item)
  
            r += 1

        return list(res)
    
    # Rabin-Karp 方法 (本题即转换为 4 进制问题)
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10: return []
        c2v = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        res = set()
        vis = set()
        window = sum(c2v[s[i]]*(4**(9-i)) for i in range(10))
        vis.add(window)

        for r in range(10, n):
            # 更新窗口值
            window = window * 4 - c2v[s[r-10]]*4**10 + c2v[s[r]]
            if window in vis:
                res.add(s[r-9: r+1])
            vis.add(window)
        return list(res)


    # 二进制掩码
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from functools import reduce
        n = len(s)
        if n <= 10: return []
        c2v = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        res = set()
        
        window = reduce(lambda a, b: a | c2v[s[b]]<<2*(9-b), range(10), 0)
        vis = set([window])

        for r in range(10, n):
            window = (window << 2) & (~(3 << 20)) | c2v[s[r]]
            if window in vis:
                res.add(s[r-9: r+1])
            vis.add(window)
            
        return list(res)
