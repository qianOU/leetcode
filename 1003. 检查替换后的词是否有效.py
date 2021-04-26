class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            # 出栈的条件
            if i == 'c':
                if len(stack) < 2:
                    return False
                else:
                    # 检查 是否 等于 b
                    item = stack.pop()
                    if item != 'b':
                        return False
                    # 检查 是否 等于 a
                    item = stack.pop()
                    if item != 'a':
                        return False
            
            else:
                stack.append(i)
        
        return not stack

                    
