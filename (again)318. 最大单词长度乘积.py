class Solution:
    # 暴力 + set
    # 优化思路：set[实际上可以优化set的空间]以及比较的次数，（对于比较次数的优化主要是 记录有相同字符的最长长度即可 ）
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        path = [set(i) for i in words]
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if not (path[i] & path[j]):
                    ans = max(ans, len(words[i])*len(words[j]))
        
        return ans
    
    # 优化 set，使用 二进制  26 位掩码，每一位 也就是 一个 字符 是否出现
    # 优化 比较的过程，使用字典来记录 二进制 的最长长度
    def maxProduct(self, words: List[str]) -> int:
        import collections
        length = [len(i) for i in words] # 长度数组
        rec = collections.defaultdict(int)

        for i in range(len(words)):
            item = words[i]
            res = 0 # 将 相同字符 压缩成 一个整数， 使用二进制位掩码来做代表
            for c in item:
                res |= 1 << (ord(c) - ord('a')) 
            
            # 只是记录有相同字符，rec[res] 记录的是有相同字符的 最长长度
            rec[res] = max(rec[res], length[i])

        # 记录字典的数组，避免下面的双重循环出现 a X b 和 b X a 的情况
        tmp = list(rec.keys())
        ans = 0
        n = len(tmp)
        for i in range(n):
            for j in range(i+1, n):
                if not (tmp[i] & tmp[j]):
                    ans = max(rec[tmp[i]]*rec[tmp[j]], ans)
            
        return ans