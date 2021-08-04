class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        m = len(str(n))
        from collections import deque
        q = deque([[i, 0, len(path[i])-1, path[i][-1]] for i in range(n)])

        while q:
            sz = len(q)
            rec = defaultdict(int)
            wanted = defaultdict(int)
            for _ in range(sz):
                i, need, idx, ch = q.popleft()
                if need:
                    res.append((i, idx, ch))
                    wanted[ch] += 1
                rec[ch] += 1
            
            for (i, idx, ch) in res:
                if wanted[ch] == rec[ch]:
                    if 
                    q.append([i, , , path[i][-1]])
                else:
                    path[i] = path[i][idx]