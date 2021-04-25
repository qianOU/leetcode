# class Solution:
#     def minTime(self, n: int, edges, hasApple) -> int:
        
#         # 后序遍历
#         def bfs():
#             from collections import defaultdict
#             records = defaultdict(set)
            
#             for idx, (i, j) in enumerate(edges):
#                 records[i].add(j)
#                 records[j].add(i)
            
#             q = [0]
#             button = [key for key, i in records.items() if len(i)==1]
            
#             ans = [0] * n # 记录 idx（索引） 的祖先节点
            
#             visited = set()
#             while q:
#                 sz = len(q)
#                 for _ in range(sz):
#                     node = q.pop(0)
#                     for i in records.get(node):
#                         if i in visited:
#                             continue
#                         visited.add(i)
#                         q.append(i)
#                         ans[i] = node
                    

            
#             print(ans)
#             # bfs
            
#             # = set(i[0] for i in button)
#             print(button, visited)
#             q = button
#             res = 0
#             visited = set([0])
#             # hasApple[0] = True
#             # print(q ,ans)
#             print(ans)
#             while q:
#                 sz = len(q)
#                 for _ in range(sz):
#                     item  = q.pop(0)
                    
#                     if  item in visited:
#                         continue
                    
#                     visited.add(item)
#                     par = ans[item]

#                     if hasApple[item]:
#                         hasApple[par] = True
                    
#                     # if  hasApple[item] and hasApple[par]:
#                     #     print(item, par)
#                     #     res +=  1 

#                     q.append(par)
                    
            
#             for u,v in edges:
#                 if hasApple[u] and hasApple[v]:
#                      res+=1       
   
#             return res*2
        
#         return bfs()
class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        import collections
        graph=collections.defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited=set()
        # n叉树的后序遍历
        def dfs(root):
            visited.add(root)
            for nex in graph[root]:
                if nex not in visited:                    
                    dfs(nex)
                    if hasApple[nex]:
                        hasApple[root]=True
        
        dfs(0)
        res=0

        for u,v in edges:
            if hasApple[u] and hasApple[v]:
                res+=1
        return res*2