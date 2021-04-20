# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dfs 搜索
    def longestZigZag(self, root: TreeNode) -> int:
        max = 0 #记录最长交错路径
        def dfs(root, state, depth):
            # state 1 表示走的左子树
            # state 0 表示走的右子树
            nonlocal max
            if root is None:
                return 
            
            # 交错路径搜索结束的位置
            if (not root.left or (root.left and state==1)) and  \
                 (not root.right or (root.right and state==0)):
                    if  max < depth:
                       max = depth 
                    return

            #如果有左子节点，并且上一轮走的是右子节点，则 路径长度加一，进行下一次决策
            if  root.left and  (state != 1):
                dfs(root.left, 1, depth+1)
            #如果有左子节点，并且上一轮走的也是左子节点，则将该节点设位根节点，路径长度设为 1，去左子节点试试运气
            if root.left:
                # 这样设置可以避免 重复搜索
                dfs(root.left.left, 1, 1) 
            #如果有右子节点，并且上一轮走的是左子节点，则 路径长度加一，进行下一次决策
            if root.right and (state != 0):
                dfs(root.right, 0, depth+1)
            #如果有右子节点，并且上一轮走的也是右子节点，则将该节点设位根节点，路径长度设为 1，去右子节点试试运气
            if root.right:
                dfs(root.right.right, 0, 1)
        
        dfs(root, None, 0)
        return max

    # 动态规划解法：
    """
    记 f(u) 为从根到节点 u 的路径上以 u 结尾并且 u 是它父亲的左儿子的最长交错路径，
    g(u) 为从根到节点 u 的路径上以 u 结尾并且 u 是它父亲的右儿子的最长交错路径。
    记 u 的父节点为father(u)，我们可以推得这样的转移方程： ​	      
        f[u]=g[father(u)]+1case
        g[u]=f[father(u)]+1​	
    """
    def longestZigZag(self, root: TreeNode) -> int:
        if root is None:
            return 0

        import collections
        # 根节点到根节点的最长交叉路径长度为 0， base-case
        f, g = collections.defaultdict(int), collections.defaultdict(int)
        
        q = [(root, None)]
        while q:
            node, par = q.pop(0)
            if par:
                if par.left == node:
                    f[node] = g[par] + 1
                else:
                    g[node] = f[par] + 1
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        # 找寻最大值
        return max(*f.values(), *g.values())

    
            

