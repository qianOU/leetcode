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
                # 如果最优路径是出界的，可以调整前后跳的顺序让其不出界，所以最优解一定在界内
                # 注意这个 6000 是怎么得来的， 参考大神数学解析
                elif cur in forbidden or cur > 6000:
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