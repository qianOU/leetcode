class Solution:
    # 思路1：递归 + 单调栈找寻 next grerat number
    # 四路2：局部有序直接使用 单调栈
    def verifyPreorder(self, preorder: List[int]) -> bool:
        n = len(preorder)
        nxt = [-1]*n
        for i in range(n-1, -1, -1):
            while stack and preorder[stack[-1]] < preorder[i]:
                stack.pop()
            
            if stack: 
                nxt[i] = stack[-1]
            stack.append(i)


        def dfs(l, r, low, hi):
            print(l, r, low, hi)
            if l >= r: return True
            if not low < preorder[l] < hi: return False 
            
            i = nxt[l] # 比 preorder[i] 大的首元素位置
            if preorder[i] > preorder[l]:
                return dfs(l+1, i-1, low, preorder[l]) and dfs(i, r, preorder[l], hi)    
            return dfs(l+1, r, low, preorder[l]) # 只有左子树的情况
        
        return dfs(0, len(preorder)-1, float('-inf'), float('inf'))
            


        