class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            stack.append(i)
            # 发生碰撞的时候，一定是第一个星体 大于 0 ，第二个星体 小于 0 的情况
            while len(stack)>=2 and stack[-1] < 0 and stack[-2] > 0:
                if abs(stack[-1]) > stack[-2]:
                    item = stack.pop() # 保留第二个星体
                    stack.pop()
                    stack.append(item)
                elif abs(stack[-1]) < stack[-2]: # 保留第1个星体
                    stack.pop()
                else:
                    stack.pop()
                    stack.pop()
        
        return stack