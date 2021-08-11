class Solution:
    # 状态压缩 + BFS （即使用二进制将节点访问情况压缩为一个字）
    # 最短路联想到BFS, 遍历到一个点由两个变量控制即 当前节点值 + 到当前节点已经遍历过的点
    # 多源BFS
    def shortestPathLength(self, graph) -> int:
        from collections import deque
        n = len(graph)
        q = deque((i, 1 << i, 0) for i in range(n))
        seen = {(i, 1 << i) for i in range(n)} 
        ans = 0
        all_down = (1 << n) - 1

        while q:
            cur, mask, dist = q.popleft()
            if mask & all_down == all_down:
                ans = dist
                break
            for nxt in graph[cur]:
                new_mask = mask | (1 << nxt)
                if (nxt, new_mask) not in seen:
                    q.append((nxt, new_mask, dist + 1))
                    seen.add((nxt, new_mask))
            
        return ans

print(Solution().shortestPathLength(
[[1, 2],
[0],
[0]]
))