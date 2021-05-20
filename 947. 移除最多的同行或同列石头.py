class Solution:
    def removeStones(self, stones) -> int:

        # 构建状态表
        rows = {}
        cols = {}
        for i, j in stones:
            rows[i] = rows.get(i, 0)  + 1
            cols[j] = cols.get(j, 0) + 1
        
        max_ = 0

        visited = set()
        def dfs(i,j, num):
            nonlocal max_
            
            # 如果 i，j 不能再 被拿走 则结束
            if rows[i] == 1 and cols[j] == 1:
                max_ = max(max_, num-1)
                return 

            
            for i1, j1 in stones:
                item = (i1, j1)
                # 使用 visited 来控制 当前 i,j 的可选项
                if item not in visited and rows[i1]>=1 and cols[j1]>=1:
                    visited.add(item)
                    rows[i1] -= 1
                    cols[j1] -= 1
                    dfs(item[0], item[1], num+1)
                    rows[i1] += 1
                    cols[j1] += 1
                    visited.discard(item)
            


        ans = 0
        visited = set()
        for i,j in stones:
            item = (i, j)
            if rows[i] <= 1 and cols[j] <= 1:
                visited.add(item)
                continue
            elif  item not in visited:
                visited.add(item)
                rows[i] -= 1
                cols[j] -= 1
                dfs(item[0],item[1], 1) # num 表示取完 item 的时候，总共用了几步
                rows[i] += 1
                cols[j] += 1
                visited.discard(item)
            print(max_)
        
        print(rows, cols)
        return max_

print(Solution().removeStones(
[[0,1],[1,2],[1,3],[3,3],[2,3],[0,2]]))