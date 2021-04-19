class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        import functools
        # dp 函数表示使用 arr[left,...right] 构建子树时，得到的每个非叶节点的值的最小可能总和
        @functools.lru_cache(None)
        def dp(left, right):
            if right == left: # 只有一个叶子节点时，返回 0
                return 0
            final_score = float('inf')
            # 找寻划分左右子树的范围，从所有可能的答案中选择最小的那个
            for k in range(left+1, right):
                # 当前节点的最小可能总和 = 左子树部分最小可能总和 + 右子树部分可能最小总和 + 根节点值
                cur = dp(left, k) + dp(k, right) + max(arr[left:k+1])*max(arr[k+1:right+1])
                final_score = min(final_score, cur)
            
            return final_score
                

        # 单调递减栈
        # 每加入一个元素，就需要弹出一个累计元素（即非叶子节点元素），使用单调栈有这个特性
        stack = [float('inf')]
        total = 0
        for i in arr:
            while i >= stack[-1]:
                total += stack.pop()* + min(i, stack[-1])
            stack.append(i)

        while len(stack) > 2:
            total += stack.pop() * stack[-1]

        return total  
