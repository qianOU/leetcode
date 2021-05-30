class Solution:
    def maxDepthAfterSplit(self, seq: str) :
        stack = []
        depth, n = 0, len(seq)
        ans = [0]*n
        for i in range(n):
            if seq[i] == '(': stack.append(i)
            elif i - stack[-1] > 1: # 嵌套情况
                item = stack.pop()
                ans[item] = 1-ans[item+1]
                ans[i] = 1-ans[item+1]
            else:
                ans[stack.pop()] = 0
                ans[i] = 0
        
        return ans

print(Solution().maxDepthAfterSplit("()(())()"))