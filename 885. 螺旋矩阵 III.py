class Solution:
    # 模拟
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        ans = [(rStart, cStart)]
        count, step = 1, 1
        tar = rows * cols
        x, y = rStart, cStart
        check = lambda x, y: 0 <= x < rows and 0 <= y < cols
        while count < tar:
            # 进行下一个螺旋状态
            if x <= rStart and y == cStart:
                step += 2
            # 右
            for i in range(step>>1):
                y += 1
                if check(x, y): 
                    count += 1
                    ans.append((x, y)) 
            
            # 下
            for i in range(step-2):
                x += 1
                if check(x, y): 
                    count += 1
                    ans.append((x, y)) 
            # 左
            for i in range(step-1):
                y -= 1
                if check(x, y): 
                    count += 1
                    ans.append((x, y))
            # 上
            for i in range(step-1):
                x -= 1
                if check(x, y): 
                    count += 1
                    ans.append((x, y))

            # 右,回到出发点
            for i in range(step>>1):
                y += 1
                if check(x, y): 
                    count += 1
                    ans.append((x, y)) 

        return ans


class Solution:
    # 官方思路，1，1，2，2，3，3，4，4，5，5，6，6，...
    # 螺旋矩阵具有自相似性质
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        x, y = rStart, cStart
        ans = [(x, y)]
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count, tar = 1, rows * cols
        step = 0
        while count < tar:
            for idx, (i, j) in enumerate(d, 1):
                if idx & 1: step += 1 # 每两个方向步数需要 + 1
                for _ in range(step):
                    x, y = x + i, y + j
                    if 0 <= x < rows and 0 <= y < cols:
                        ans.append((x, y))
                        count += 1
        return ans


print(Solution().spiralMatrixIII(
1,
4,
0,
0
))