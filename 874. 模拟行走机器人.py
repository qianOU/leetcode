class Solution:
    def robotSim(self, commands, obstacles) -> int:
        ans = 0
        state = [0, 0]
        obts = set(tuple(i) for i in obstacles)
        flag = 0 # 左转 + 1, 右转 - 1 
        # 因为左转或者右转可以相互抵消，因此使用计数来表示，并且注意 4 为一周期
        # direct 是 方向字典
        direct = {0:(0, 1), 1:(1, 0), 2:(0, -1), 3:(-1, 0)}
        for i in commands:
            if i == -1:
                flag += 1
            elif i == -2:
                flag -= 1
            else:
                item = flag % 4
                u, v = direct[item]
                for j in range(1, i+1):
                    x, y = state[0] + u*j, state[1] + v*j
                    if (x, y) in obts:
                        state = [x-u, y-v]
                        break
                
                if (x, y) not in obts:
                    state = [x, y]
                
                ans = max(ans, state[0]**2 + state[1]**2)
                print(ans, item, (u, v), state)
        return ans

print(Solution().robotSim(
[-2,-1,-2,3,7],
[[1,-3],[2,-3],[4,0],[-2,5],[-5,2],[0,0],[4,-4],[-2,-5],[-1,-2],[0,2]]
))
