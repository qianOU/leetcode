class Solution:
    def rotateTheBox(self, box):
        # 先下沉 再翻转
        m, n = len(box), len(box[0])
        for row in box:
            # 使用快慢指针 直接在原数组进行更改
            slow =  n-1 
            for fast in range(n-1, -1, -1):
                if row[fast] == '*':
                    slow = fast - 1
                if row[slow] != '*' and row[fast] == '#':
                    row[slow] = row[fast]
                    # 如果 fast 在 slow 之前，因为fast 的 石头移动到了 slow 位置， 所以 fast位置清空
                    if fast < slow:
                        row[fast] = '.'
                    slow -= 1

        matrx = [[0]*m for i in range(n)]
        for i in range(m):
            for j in range(n):
                matrx[j][i] = box[m-1-i][j]

        return matrx

print(Solution().rotateTheBox(
[["*","#","*",".",".",".","#",".","*","."]]
))