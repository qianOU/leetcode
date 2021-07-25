class Solution:
    # 分治算法，存在子问题的情况
    # 返回 expression 的所有可能的结果
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit(): return [int(expression)]
        
        res  = []
        for i in range(len(expression)):
            if expression[i] in '+-*': # 以 i 为最后一步结合的符合进行枚举
                right = self.diffWaysToCompute(expression[i+1:])
                left = self.diffWaysToCompute(expression[:i])
                for l in left:
                    for r in right:
                        if expression[i] == '+':
                            res.append(l + r)
                        elif expression[i] == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        
        return res