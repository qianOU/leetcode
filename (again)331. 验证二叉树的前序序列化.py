class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        items = preorder.split(',')
        if not items:
            return False

        # 基于递归特性
        def dfs(state):
            # 如果左子树有字符匹配，但是右子树没有字符匹配，则是不合法的
            if not items and state == 1: # 右子树
                return False
            # 如果左右子树都有匹配字符则是合法的
            elif not items and state == 0: # 左子树
                return True

            # 弹出根节点
            item = items.pop(0)
            # 如果是 # 返回 True， 不向下匹配 子树
            if item == '#':
                return True
            # 根据前序遍历特性，遍历 左子树与右子树
            return dfs(0) and dfs(1)
        
        # 返回结果，并且判断items 是否为空 来避免树的最后的#之后，有字符出现
        return dfs(None) and not items
    
    # 方法2： 自底向上 栈 模拟递归
    def isValidSerialization(self, preorder: str) -> bool:
        items = preorder.split(',')
        stack = []
        for i in items:
            stack.append(i)
            while len(stack) >=3 and stack[-1] == '#' and stack[-2] == '#':
                stack.pop()
                stack.pop()
                stack.append('#')
        
        return len(stack) == 1 and stack[-1] == '#'
    
    # 方法3： 基于树的出度和入度相等的特性
    def isValidSerialization(self, preorder: str) -> bool:
        items = preorder.split(',')
        diff = 1 # 初始化 入度 - 出度 为 1
        for i in items:
            diff -= 1 # 添加一个新节点，入度减一
            if diff < 0:
                return False
            if i != '#':
                diff += 2
        
        return diff == 0





        
