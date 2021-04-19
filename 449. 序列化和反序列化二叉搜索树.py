# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方式一： 前序遍历 + 二分查找
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ''
        # 记录前序遍历的结果
        return str(root.val)+',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        ans = [int(i) for i in data.split(',') if i.isdigit()]
        # 使用二分查找，找寻大于 root 节点的第一个元素的位置
        # [start, end]
        def bin_search(start, end, target):
            left = start
            right = end
            # 找寻左边界
            while left <= right:
                mid = left + (right-left)//2
                if ans[mid] < target:
                    left = mid + 1
                else:
                    right = mid  - 1 
            
            return left
        
        def dfs(start, end):
            if start > end:
                return
            root = TreeNode(ans[start])
            idx = bin_search(start+1, end, ans[start])
            root.left = dfs(start+1, idx-1)
            root.right = dfs(idx, end)
            return root
        
        return dfs(0, len(ans)-1)




# 方案 二 后序遍历存储序列化结果
# 反序列化 使用 参数限制子树生长的范围区间
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ''
        # 记录前序遍历的结果
        return self.serialize(root.left) + ',' + self.serialize(root.right) + ',' + str(root.val) 
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        ans = [int(i) for i in data.split(',') if i.isdigit()] # 后序遍历的结果
        def dfs(lower, upper):
            # 如果遍历结束，或者 当前遍历的节点值不在 lower 或者 upper 范围内， 需要回溯到上一个节点进行插入处理
            if not ans or ans[-1] < lower or ans[-1] > upper:
                return None

            item = ans.pop()
            root = TreeNode(item) #弹出根节点   
            # 由于是后序遍历还原所以需要先还原右子树
            root.right = dfs(item, upper) # 更新右子树的插入范围
            root.left = dfs(lower, item) # 更新左子树的插入范围
            return root 
        
        return dfs(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans