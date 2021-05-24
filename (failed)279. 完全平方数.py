class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n
        # 得到所有可能的 组合数 排除 1   
        selects = []
        for i in range(int(n**.5), 1, -1):
            if i**2 > n:
                break
            selects.append(i**2)
        # 数和索引的映射表
        records = {j:i for i,j in enumerate(selects)}
        
        from collections import deque
        q = deque([(n, selects[0])])
        count = 0 # 记录层次遍历的次数
        min_x = float('inf')

        while q:
            length = len(q)
            for _ in range(length):
                # 记录上一次的选择，是为了确保得到的序列是单调非减序列
                cur, prev = q.popleft() # cur, prev 分别指当前节点以及 上一步的选择
                if not cur or min_x <=count: # 如果 在最小层次 得到了可行解，就退出搜索
                    return min(min_x, count)
                if cur < selects[0]: # 只能加 1 的情况
                    min_x = min(min_x, count + cur)
                
                for j in selects[records[prev]:]:
                    if cur - j>=0:
                        q.append((cur - j, j))

            count += 1
        
        return min_x


print(Solution().numSquares(6255))