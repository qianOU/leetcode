# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs + 使用集合的方式记录点
class FindElements:

    def __init__(self, root: TreeNode):
        if root is None:
            self.root = root
            return 
        
        def dfs(root, par, state=0): 
            if state == 1: #左子节点
                root.val = 2*par + 1
            elif state == 2:
                root.val = 2*par + 2

            self.records.add(root.val)


            if root.left:
                dfs(root.left, root.val, 1)
            if root.right:
                dfs(root.right, root.val, 2)
        
        self.records = set(0) #记录树的节点值
        dfs(root, 0, 0)
        self.root = root

    # 使用集合
    def find(self, target: int) -> bool:
        if not self.root:
            return False
        return target in self.records

# dfs + 二叉树的 二进制表示
class FindElements:

    def __init__(self, root: TreeNode):
        if root is None:
            self.root = root
            return 
        
        def dfs(root): 
            if root.left:
                root.left.val = 2*root.val + 1 
                dfs(root.left)
            if root.right:
                root.right.val = 2*root.val + 2
                dfs(root.right)
        

        dfs(root)
        self.root = root

    # 使用集合
    def find(self, target: int) -> bool:
        if not self.root:
            return False
        target = target + 1 # 将第 h 层 中节点总数 控制位 [2^h, 2^(h+1)-1]
        params = 1 << (len(bin(target)) - 4) # 将param中 1移动到次高位
        tmp = self.root
        while tmp is not None and params > 0:
            if params & target:
                tmp = tmp.right
            else:
                tmp = tmp.left
            
            params >>= 1
        
        return params == 0 and tmp is not None



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)