class Solution:
    # 排序 和 遍历的 顺序是只 十分重要的 
    def carFleet(self, target: int, position, speed) -> int:
        n, stack = len(speed), []
        time = [-(target-position[i])/speed[i] for i in range(len(speed))]

        time = sorted(zip(position, time), reverse=True) # 将离终点近， 以及速度快的 顺序排序
        # stack 是单调递增栈， 其中的栈顶元素是目前车队到达终点的最长时间
        i = 0
        # 优先遍历 离 终点近的车辆
        while i < n:
            _, stamp = time[i]
            if stack and stack[-1] >= -stamp:
                i += 1
                continue
            stack.append(-stamp)
        
        return len(stack)

print(Solution().carFleet(12,
[10,8,0,5,3],
[2,4,1,1,3]))