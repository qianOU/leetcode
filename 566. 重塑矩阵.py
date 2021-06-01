class Solution:
    
    def matrixReshape(self, mat, r: int, c: int):
        m, n = len(mat), len(mat[0])
        if m*n != r*c: return mat
        ans = []
        cum = 0
        for i in range(r):
            r1, c1 = divmod(cum, n)
            
            count, res = 0,  []
            print(cum, r1, c1, ans)
            for row in range(r1, m):
                for j in range(c1, n):
                    if count == c:
                        break
                    res.append(mat[row][j])
                    count += 1
                
                c1 = 0
            
            ans.append(res)
            cum += c
        return ans
                

print(Solution().matrixReshape(
[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
,4
,5
))