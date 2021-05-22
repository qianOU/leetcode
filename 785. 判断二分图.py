class Solution:
    def isBipartite(self, graph) -> bool:
        n = len(graph)
        # 状态 列表 1， -1 各自代表不同的集合 ， 0 代表未遍历的元素
        status = [0] * n

        def dfs(i, prev):
            # 如果 一根 线的两端在同一个集合 则 返回 False
            if prev is not None and status[i]*status[prev]==1:
                return False
            # 否则的话， 根据 i 的状态 取为 prev 的 相反状态
            status[i] = -1 * status[prev] if prev is not None else 1

            for j in graph[i]:
                if not status[j] and not dfs(j, i): # 如果还没遍历过 j
                    return False
                elif status[j]*status[i]==1: # 如果和之前的矛盾
                    return False
            
            return True
        
        for i in range(n):
            if not status[i]: # 如果未遍历
                if not dfs(i, None):
                    return False

        return True