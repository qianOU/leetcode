"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    # 因为要建立 前，后节点之间的关系，因此 递归参数需要两个， 即 前继节点与当前节点
    def flatten(self, head: 'Node') -> 'Node':
        
        if not head:
            return head

        # 前序遍历
        def dfs(pre, curr): 
            """
            在遍历过程中，构建新的节点关系，并且只返回某一条链路最后的结点，
            以便用于与右子链路构建关系
            """
            if curr is None: # base-case
                return pre
            
            # 建立前后结点之间的关系
            curr.prev = pre
            pre.next = curr
            
            tmp = curr.next
            if curr.child: # child 相当于左子树
                tail = dfs(curr, curr.child) # 处理左子树
                curr.child = None

                return dfs(tail, tmp) # 处理右子树
            
            return dfs(curr, tmp) # 只有右子树的时候
        
        dum = Node(0, None, head, None)
        head.prev = dum

        dfs(dum, head)
        # 注意一定要 取消 head 的前继结点
        dum.next.prev =None
        
        return dum.next
    
    # 使用前序遍历的迭代方式， 主题记得使用 prev 指向前继结点
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        dum = Node(0, None, head, None)
        head.prev = dum
        
        prev = dum
        stack = [head]

        while stack:
            item = stack.pop()
            prev.next = item
            
            if not item: # 如果是 None
                continue

            item.prev = prev # 1-2 构建前后节点之间的关系
            stack.append(item.next) # 先右子树入栈，其次如果存在左子树，则左子树后入栈

            if item.child:
                stack.append(item.child)
                item.child = None
        
            prev = item # 更新前继节点
        
        dum.next.prev = None
    
        return  dum.next