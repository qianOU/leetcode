class Solution:
    # 括号匹配问题， 嵌套深度概念十分重要
    # 要使得拆分后的嵌套深度最小，也就是 对于 seq 中的嵌套深度，进行交替换取
    # 比如 5层 seq 可以这么分 : 0-1-0-1-0 得到最小的嵌套深度为 3
    # 交替分的逻辑可以使用嵌套深度的奇偶性区分
    def maxDepthAfterSplit(self, seq: str) :
        d = 0 # 记录嵌套深度
        ans = []
        for i in seq:
            if i == '(':
                d += 1
                ans.append(d % 2)
            else:
                ans.append(d % 2)
                d -= 1
            
        return ans

print(Solution().maxDepthAfterSplit("((()(()((()()))((()()((()(()(()())(()(()))))))))))"))