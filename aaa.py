 # 方法2： 拓扑排序 BFS
def eventualSafeNodes(graph):
    n = len(graph)
    outdegree = [0] * n
    rgraph = [[] for i in range(n)]

    for i in range(n):
        outdegree[i] = len(graph[i]) # 原视有向图节点的出度，也就是逆转图的入度
        for j in graph[i]:
            rgraph[j].append(i)
    
    from collections import deque
    q = deque()
    # 将出度为 0 的入队列
    for i in range(n):
        if not outdegree[i]:
            q.append(i)
    
    safe = [False] * n
    while q:
        cur = q.popleft()
        safe[cur] = True
        for j in rgraph[cur]:
            outdegree[j] -= 1
            if not outdegree[j]:
                q.append(j)

    return [i for i in range(n) if safe[i]]


print(eventualSafeNodes([[0]]))