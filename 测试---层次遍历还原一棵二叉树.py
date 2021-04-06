# 由层次遍历，还原一棵二叉树
def back_tree(nums = [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]):
    root =  TreeNode(nums.pop(0))
    queue = []
    queue.append(root)

    while len(queue) and len(nums):
       q = queue.pop(0)
       if q is None:
           continue
       q.left = TreeNode(nums.pop(0)) if nums[0] is not None else nums.pop(0) # 如果是 None 叶修要弹出
       q.right = TreeNode(nums.pop(0)) if nums[0] is not None else nums.pop(0)
       queue.append(q.left)
       queue.append(q.right)
       print(queue)

    return root

import queue
# 层次遍历 
# 不需要借助 于 递归
# 主要需要借助于 队列 来实现
def layer_serializer(root):
    if root is None: return
    q = queue.Queue() # 队列用于存放，每一层的节点
    q.put(root) # 根节点入队列
    st = [] # 存放遍历路径
    while not q.empty():
        cur = q.get()
        
        if cur is None:
            st.append('NULL')
        else:
            st.append(str(cur.val))
            q.put(cur.left)
            q.put(cur.right)
            
    return ''.join(st)