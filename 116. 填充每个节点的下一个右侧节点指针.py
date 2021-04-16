class Solution:
    # BFS
    def connect(self, root: 'Node') -> 'Node':
        from collections  import deque
        if root is None:
            return
        
        ans = root
        q = deque([root])

        # 写的较为复杂，有精简版
        # while q:
        #     sz = len(q)
        #     for i, _ in enumerate(range(sz)):
        #         if not i:
        #             prev = q.popleft()
        #             prev.next = None
        #             if prev.left:
        #                 q.append(prev.left)
        #             if prev.right:
        #                 q.append(prev.right)
        #             continue
        #         top = q.popleft()
        #         prev.next = top
        #         if top.left:
        #             q.append(top.left)
        #         if top.right:
        #             q.append(top.right)
        #         top.next = None
        #         prev = top

        # 模板
        while q:
            sz = len(q)
            for  i in range(sz):
                top = q.popleft()
                if i < sz - 1:
                    top.next = q[0] # 可以用索引的方法获取队列的第一个元素，且不用出队列
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
        return ans
    
    def connect(self, root: 'Node') -> 'Node':
        # 递归版本，前序遍历
        def dfs(root):
            if root is None:
                return
            if root.left:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return root
        
            