class Solution:
    # 解法1： DFS 解法
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        res = []
        
        def dfs(cur):
            if cur >= n:
                return
            
            tmp = ['' for i in range(numRows)]
            for i in range(cur, min(cur + numRows, n)):
                tmp[i - cur] = s[i]

            cur = i + 1
            res.append(tmp)

            for i in range(numRows-2, 0, -1):
                if cur >= n: break
                tmp = ['' for i in range(numRows)]
                tmp[i] = s[cur]
                res.append(tmp)
                cur += 1
            
            dfs(cur )

        dfs(0)

        cols = len(res)
        print(res)
        return ''.join(''.join(res[row][col] for row in range(cols)) for col in range(numRows))


    # 解法2： 遍历字符串，将字符放到对应的行中
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = ['' for i in range(min(numRows, len(s)))]
        # 使用一个变量 记录 是向上还是向下 
        cur = 0
        step = 1  # 控制方向的

        for i in s:
            res[cur] += i
            cur += step
            # 如果到达了最低行，或者首行 需要 转换 方向
            if cur + step < 0 or cur + step == numRows:
                step *= -1

        return ''.join(res)


    # 解法3： 直接遍历行，每次优先填充遍历的那一行
    def convert(self, s: str, numRows: int) -> str:
        rows = min(len(s), numRows)
        base = 2*numRows - 2

        n = len(s)
        ans = ''
        for row in range(rows):
            for cur in range(row, n, base):
                ans += s[cur]
                # 对于 [1, rows-2] 中的每一行都有两个值
                if 0 < row < rows-1 and cur  + base - 2*row < n:
                    ans += s[cur  + base - 2*row] 
        return ans


print(Solution().convert(
"PAYPALISHIRING",
3
))