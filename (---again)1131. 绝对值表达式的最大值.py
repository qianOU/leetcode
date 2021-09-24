class Solution:
    # 数学：绝对值展开，发现有8种情况,由于i。j的对称性所以实质上是4种情况
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        d = ((1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1)) 
        ans = 0
        max_ = [float('-inf')]*4
        for p in range(4):
            for i in range(n):
                x, y, z = d[p]
                max_[p] = max( max_[p],
                arr1[i]*x + arr2[i]*y + i*z
                )

        ans = 0
        for p in range(4):
            for i in range(n):
                x, y, z = d[p]
                ans = max( ans,
                max_[p] - (arr1[i]*x + arr2[i]*y + i*z)
                )
                
        return ans