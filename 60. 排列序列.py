class Solution:
    # 贪心 + 递归
    def getPermutation(self, n: int, k: int) -> str:
        from functools import reduce
        
        def dfs(k, path):
            if not k: return ''.join(str(i) for i in path[::-1])
            elif k <= 1: return ''.join(str(i) for i in path)
            n = len(path)
            idx, res = divmod(k, reduce(lambda x, y: x*y, range(1, n), 1))
            idx = idx if res else idx - 1 # 是否被整除意味着字符串左起第一个字符是否需要改变
            one = path[idx]
            path.pop(idx) # 弹出 处理子问题
            return str(one) + dfs(res, path)
        
        return dfs(k, list(range(1, n+1)))