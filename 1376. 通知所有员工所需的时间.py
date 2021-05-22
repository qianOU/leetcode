class Solution:
    # 方法 一 ：BFS  维护路径的时间和， 最后获取  路径时间最长的答案
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        # 构建 上司 和 下属的关系表
        sub = [[] for i in range(n)]
        for i,j in enumerate(manager):
            if j == headID:
                sub[headID].append(i)
            elif j != -1:
                sub[j].append(i)
        
        from queue import deque
        q = deque([(headID, 0)])
        ans = 0
        while q:
            sz = len(q)
            layer_max = 0
            for _ in range(sz):
                cur, score = q.popleft()
                score += informTime[cur]
                if not sub[cur]:
                    ans = max(ans, score)
                for i in sub[cur]:
                    q.append((i, score))
   
        return ans

    # 方法 二 ：DFS  后序遍历  获取  路径时间最长的答案
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        # 构建 上司 和 下属的关系表
        sub = [[] for i in range(n)]
        for i,j in enumerate(manager):
            if j == headID:
                sub[headID].append(i)
            elif j != -1:
                sub[j].append(i)

        # n 叉树 的后序遍历
        def dfs(i):
            # 到达叶子节点
            if not sub[i]:
                return 0
            # n 条路径
            return max(informTime[i]+dfs(j) for j in sub[i])
        
        return dfs(headID)


print(Solution().numOfMinutes(11,
4,
[5,9,6,10,-1,8,9,1,9,3,4],
[0,213,0,253,686,170,975,0,261,309,337]))