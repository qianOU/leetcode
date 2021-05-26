class Solution:
    # 邻接表 + DFS + visited 记录
    def accountsMerge(self, accounts):
        n = len(accounts)
        from collections import defaultdict
        records = defaultdict(list)
        # 邻接表
        for idx, num in enumerate(accounts):
            for j in num: records[j].append(idx)
        
        visited = [False]*n
        res = []

        # 获得 与 account[id] 同一个账号的所用 索引
        def dfs(id):
            ans = [id]
            if visited[id]: return []
            visited[id] = True

            for email in accounts[id][1:]:
                for i in records[email]:
                    if not visited[i]:
                        ans.extend(dfs(i))
            
            return ans

        for i in range(n):
            if not visited[i]:
                items = dfs(i)
                emails = set(sum([accounts[j][1:] for j in items], []))
                ans = [accounts[items[0]][0], *sorted(emails)]
                res.append(ans)
        
        return res

print(Solution().accountsMerge(
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
))