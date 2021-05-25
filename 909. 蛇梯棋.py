class Solution:
    # 贪心 + BFS
    # 贪心思路是： 每次尽力多走几步， 不走梯子的话，需要走到最后一个 baord 为 -1 的地方
    # 遇见梯子或 蛇的话 需要入队列遍历，因为可能具有内在的最少步数
    # 使用 visit 记录路径，避免重复遍历
    def snakesAndLadders(self, board) -> int:
        n = len(board)
        target = n**2
        # x 与坐标的转换函数
        change = lambda num : (n-1-(num-1)//n, n-1-(num-1)%n if (num-1)//n%2 else (num-1)%n)
        
        from collections import deque
        q = deque()
        q.append(1)
        visited = set([1])

        count = 0
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                if cur == target:
                    return count

                flag = 0 # 设置是否 方案选择中，是否含有 board[x][y]==-1 可以走，贪心只取最大
                for i in range(1, 7):
                    x = cur + i
                    if x > target:
                        break
                    r, c = change(x)
                    
                    if 0<=r<n and 0<=c<n and board[r][c] >0 and board[r][c] not in visited:
                        visited.add(board[r][c])
                        visited.add(x)
                        q.append(board[r][c])
                    
                    if board[r][c] < 0 and x not in visited:
                        flag = 1
                        next_one = x
                
                # 贪心
                if flag:
                    r, c = change(next_one)
                    q.append(next_one)
                    visited.add(next_one)

            count += 1
        
        return -1

print(Solution().snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))