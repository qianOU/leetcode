class Solution:
    def kthLargestValue(self, matrix, k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for i in range(m)]
        #base case
        dp[0][0] = matrix[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] ^ matrix[i][0]
        
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] ^ matrix[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = matrix[i][j] ^ dp[i-1][j-1] ^ dp[i-1][j] ^ dp[i][j-1]
        
        nums = []
        for i in dp:
            nums.extend(i)
        
        print(dp, nums)
        del dp

        # 快排找寻 k 大
        import random

        def find(left, right, k): # 闭区间
            
            idx = random.randint(left, right)
            t = nums[idx]
            # 将 t 交换到最后一个位置
            nums[idx], nums[right] = nums[right], nums[idx]

            l, r = left, right - 1
            while l <= r:
                while l <= r and nums[l] < t:
                    l += 1
                
                while l <= r and nums[r] > t:
                    r -= 1
                
                if l>=r: break
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1

            # nums[l] 可能大于等于 t
            nums[l], nums[right] = nums[right], nums[l]
            # 查看区间[left...l]是否有k个元素
            if l - left + 1 == k:
                return t
            elif l - left + 1 > k:
                # 在[left, l-1/r] 中寻找 k 个元素
                return find(left, l-1, k)
            else:
                # 在[l+1, right] 找寻 k-(l-left+1) 个元素
                return find(l+1, right, k-(l-left+1))

        return find(0, len(nums)-1, len(nums) - (k-1)) 
        # return find(59, 60, 2) 


print(Solution().kthLargestValue( 
[[0,9,5,8,2,2,0,10,0,5,8,6,2,6,6],[7,3,3,2,9,9,8,4,1,10,7,10,2,6,9],[9,8,1,10,4,2,1,9,9,3,0,6,7,6,5],[1,1,0,7,6,0,9,2,7,1,1,4,10,10,1],[8,9,2,2,8,9,2,2,5,9,6,1,10,7,5]]
,15
))