class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        if len(pushed) != len(popped):
            return False

        check = [] # 辅助栈序列
        j = 0
        for i in pushed:
            check.append(i) # pushed 序列依序入栈
            while check and check[-1] == popped[j]: # 如果辅助栈顶元素与 popped序列一致，执行出栈
                j += 1
                check.pop()

        # print(check, j)
        return j == len(popped) and not check