class Solution:
    def minimumJumps(self, forbidden, a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        visited = set()
        from collections import deque
        q = deque()
        q.append((0, 0))
        visited.add(0)

        count = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                cur, back_time = q.popleft()
                # print(cur, back_time)
                if cur == x:
                    return count
                elif cur in forbidden:
                    continue
                else:
                    # 0 代表到 cur + a 是前进的步骤
                    if (cur + a, 0) not in visited:
                        visited.add((cur + a, 0))
                        q.append((cur+a, 0))

                    # 1 代表到 cur - b 是后退的步骤
                    if not back_time and cur - b>=0 and (cur - b, 1) not in visited:
                        visited.add((cur-b, 1))
                        q.append((cur-b, 1))

            count += 1
        
        
        return -1

print(Solution().minimumJumps([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
,29
,98
,80))