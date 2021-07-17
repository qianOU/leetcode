class Solution:
    # 4 基于迭代器的做法 递归做法 # 后序遍历
    # 1. 基于 n-1 的结果 顺序 前缀 + 0
    # 2. 基于 n-1 的结果，逆序 前缀 + 1
    # 上述两步得到最后的就是 n 时候的格雷编码
    def grayCode(self, n: int) -> List[int]:
        total = 2**n
        def dfs(n):
            if n == 0:
                yield from   ['0']
                return 

            elif n == 1:
                yield  from ['0', '1']
                return 
            
            before = dfs(n-1)
            tmp = []
            for i in before:
                tmp.append('1' + i)
                yield '0' + i
            while tmp: yield tmp.pop()

        
        return [int(i, base=2) for i in dfs(n)]
        
    # 基于迭代的位运算 上述过程的位运算实现
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            tmp = [(1 << i)| j for j in res[::-1]]
            res.extend(tmp)
        return res

        
            
