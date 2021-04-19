class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        import collections
        map_ = collections.defaultdict(set)
        
        n = len(edges) #得到节点数

        roots = list(range(n+1))

        def isconnect(a, b):
            root_a = get_root(a)
            root_b = get_root(b)
            return root_a == root_b
        
        def union(a, b):
            # 将b接在a上
            root_a  = get_root(a)
            root_b = get_root(b)
            roots[root_b] = root_a


        def get_root(i):
            root = i
            while root != roots[root]:
                # 路径压缩
                roots[root] = roots[roots[root]]
                root = roots[root]
            
            return root
        
        for i,j in edges:
            if isconnect(i, j): # 如果i，与 j 已经是连通的状态，如果再链接就会形成环
                return [i, j] # 返回能够构成环的边
            union(i, j)