class Solution:
    # 解法一： 基于邻接表的 bfs
    def minReorder(self, n: int, connections) -> int:
        res = 0
        records = [[] for i in range(n)]
        for idx, (i,j) in enumerate(connections):
            records[i].append(idx) # 记录节点 i 所在的边 索引
            records[j].append(idx) # 记录 节点 j 所在的边索引
        
        q = [0] # 将 0 作为根节点
        visited = [False] * (n-1) # 记录边是否被遍历过
        while q:
            top = q[0] #记录当前节点的数值
            ans = q.pop(0)
            for idx in records[top]: # 遍历所有含有 top 节点的边，也就是树向下层遍历
                i, j = connections[idx]
                if visited[idx]: # 如果这条边已经走过
                    continue
                visited[idx] = True

                if i == top: # 如果起点与树根一致，需要调整方向
                    res += 1
                    q.append(j)
                else:
                    q.append(i)
        
        return res

    # 解法二： 基于 轮询 + 集合（集合是指已经可以与0互通的节点）
    # 从所有列表中，不断轮询节点，将与 0 节点互通的那些点但是方向不对的优先进行调整
    def minReorder(self, n: int, connections):
        connected = {0} # 代表与 0 的连通状态的集合
        res = 0
        while len(connected) != n:
            not_connect = [] # 用于剪枝，去掉已经遍历过的边
            for i,j in connections:
                if i in connected:
                    res += 1
                    connected.add(j)
                elif j in connected:
                    connected.add(i)
                else:
                    not_connect.append([i,j])
            connections = not_connect 
        
        return res