class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        start = tuple(s)
        visited = set(start)
        fun = lambda x, a: str((int(x)+a)%10)

        from collections import deque
        q = deque([start])

        min_ = '9'*n
        while q:
            cur = q.popleft()
            min_ = min(min_, ''.join(cur))

            # 选择 1
            one = []
            for i, j in enumerate(cur):
                tmp = cur[i]
                if i%2:
                    tmp = fun(j, a)
                one.append(tmp)
            one = tuple(one)
            if one not in visited:
                q.append(one)
                visited.add(one)

            # 选择2
            two = (*one[n-b:], *one[:n-b])
            if two not in visited:
                q.append(two)
                visited.add(two)

        return min_