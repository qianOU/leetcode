class Solution:
    def openLock(self, deadends, target: str) -> int:
        dead = set(deadends)
        start = '0000'
        visited = set([start])
        d = [[str(i-1) if (i-1)>=0 else '9', str(i+1) if i+1 < 10 else '0'] for i in range(10)]
        print(d)

        from collections import deque
        q = deque([start])
        
        count = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                x = q.popleft()
                if x in deadends:
                    continue
                elif x == target:
                    return count 

                # 记录已经遍历节点
                visited.add(x) 
                x =  list(x)
                
                for i in range(len(x)):
                    tmp = x.copy()
                    for s in d[int(x[i])]:
                        tmp[i] = s
                        new = ''.join(tmp)
                        if new not in visited:
                            visited.add(new)
                            q.append(new)

            count += 1
        
        return  -1



print(Solution().openLock(['8888'], '0009'))

