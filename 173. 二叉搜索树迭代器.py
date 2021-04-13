# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 基于 python yield 构造的迭代器
# class BSTIterator:

#     def __init__(self, root: TreeNode):
#         self.flag = 1 # 记录第一次的欲激活状态
#         self.iter = self.iterator(root) # 迭代器
#         self.iter.send(None) # 欲激活，产出一个无关的值
#         self.total = self.count_nodes(root) # 记录比较是否遍历完所有的节点
    
#     # 查看树总共有几个节点 
#     def count_nodes(self, root):
#         if root is None:
#             return 0
#         return self.count_nodes(root.left) + self.count_nodes(root.right) + 1

#     def iterator(self, root):
#         if root is None:
#             return 
        
#         yield from self.iterator(root.left)
#         if self.flag:
#             yield 'begin'
#             self.flag = 0
#         self.total -= 1 # 在产出值之前提前减一
#         yield root.val
        
#         yield from self.iterator(root.right)

#     def next(self) -> int:
#         return next(self.iter)

#     def hasNext(self) -> bool:
#             return self.total > 0 


# 基于 数据结构 栈的倒序输出的特性实现
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.cur = root
        self.stack = []
    
    def next(self) -> int:
        # 使用栈 实现 惰性迭代
        while self.cur is not None:
            self.stack.append(self.cur)
            self.cur = self.cur.left

        top = self.stack.pop() # 推出栈顶元素
        self.cur = top.right
        return top.val 


    def hasNext(self) -> bool:
            return bool(self.stack) 


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()