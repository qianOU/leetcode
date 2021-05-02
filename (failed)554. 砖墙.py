class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
            m = len(wall)
            cum = [[0] for i in range(m)]
            for i in range(m):
                for j in range(wall[i]):
                    cum[i].append(cum[-1] + j)
            
            def back_trace(row, left, right, ans): # 左开右开
                if row == m:
                    return ans
                
                for idx in range(len(cum[row])):
                    width = cum[row][idx]
                    if left < width < right:
                        back
