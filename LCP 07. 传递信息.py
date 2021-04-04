class Solution(object):
    # BFS 
    def numWays(self, n, relation, k):
        """
        :type n: int
        :type relation: List[List[int]]
        :type k: int
        :rtype: int
        """
        path = dict()
        for i, j in relation:
            path[i] = path.get(i, []) + [j]
        print(path)
        q = []
        q.append(0)
        count = 0
        ans = 0
        while len(q)  and count <= k:
            sz = len(q)
            for i in range(sz):
                
                one = q.pop(0)
                if one == n-1 and count == k:
                    ans += 1
                for j in path.get(one,[]):
                    q.append(j)
            count += 1
        return ans

    # 动态规划 
    def numWays(self, n, relation, k):
        """
        :type n: int
        :type relation: List[List[int]]
        :type k: int
        :rtype: int
        """
        path = dict()
        for i, j in relation:
            path[j] = path.get(j, []) + [i]

        dp = [[0] * n for i in range(k+1)]
        # dp[i][j] 指的就是 第 i轮传递给编号 j 的人的方案数
        # base - case
        dp[0][0] = 1
        
        for i in range(1, k+1):
            for j in range(n):
                dp[i][j] = sum(dp[i-1][x] for x in path.get(j, []))
        
        return dp[k][n-1]

A = Solution()
print(A.numWays(3, [[0,2],[2,1]], 2))