class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        # 得到左右边界
        right = ['9'] * n
        left = ['1'] + ['0'] * (n-1)
        d = [[] for i in range(10)]

        for i in range(10):
            #  默认了每个 i 对应的选项都是 单调 递减的
            if i + k < 10:
                d[i].append(str(i+k))
            if i - k >=0 :
                d[i].append(str(i-k))    

        # 去掉前导 0 的可能性
        while '0' in d[0]:
            d[0].pop()
        
        visited = set()
        ans = []

        from collections import deque
        q = deque()
        for i in range(1, 10):
            q.append([str(i)])

        while q:
            cur = q.popleft()
            if len(cur) == n:
                item = ''.join(cur)
                if item not in visited:
                    ans.append(item)
                    visited.add(item)
                
                continue
            
            for i in d[int(cur[-1])]:
                tmp = cur.copy()
                tmp.append(i)
                q.append(tmp)
        

        return ans


print(Solution().numsSameConsecDiff(3, 7))



        
