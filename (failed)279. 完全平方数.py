class Solution:
    def numSquares(self, n: int) -> int:
        selects = []
        for i in range(int(n**.5), 1, -1):
            if i**2 > n:
                break
            selects.append(i**2)
        
        area = set(selects)
        for i in selects:
            ans = set(i*j for j in range(2, int(n/i)+1))
            area = area | ans

        print(selects, area)
        from collections import deque
        q = deque([n])

        count = 0
        while q:
            length = len(q)
            for _ in range(length):
                cur = q.popleft()
                if not cur:
                    print(cur, count)
                    return count
                
                for i in selects:
                    if cur - i in area:
                        q.append(cur - i)
            count += 1
        
        return count


print(Solution().numSquares(14))