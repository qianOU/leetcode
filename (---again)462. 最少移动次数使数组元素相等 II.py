class Solution:
    # 贪心的规则( wrong)
    def minMoves2(self, nums) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, n - 1
        ans = 0

        while l < r - 1:
            item1 = nums[l+1] - nums[l]
            item2 = nums[r] - nums[r-1]
            if item1*(l + 1) > item2*(n - r):
                ans +=  item2*(n - r)
                r -= 1
            else:
                ans += item1*(l + 1)
                l += 1

        return ans

    # 脑经急转弯，实际上最佳的移动位置是 中位数位置
    # PS: 对于 区间两侧 其 到其 区间内任意 1 点的移动次数都是固定的，为 r - l
    #  比如 [1,2,3,4] 1，4 移动到[1, 4] 之间任意一点都是固定的步数 4-1 = 3， 之后就可以看子问题 [2, 3] 之间，最后就可以锁定到中位数位置是最佳的
    
    # 基于二分选择 的 找寻 中位数的方法
    def minMoves2(self, nums) -> int:
        n = len(nums)
        
        # 找寻 第 k 小的数字
        def quick(left, right, k):
            if left == right:
                return nums[left]
                
            import random
            idx = random.randint(left, right)
            nums[idx], nums[right] = nums[right], nums[idx]
            l = left - 1
            for i in range(left, right):
                if nums[i] < nums[right]:
                    l += 1
                    nums[l], nums[i] = nums[i], nums[l]
            
            l += 1
            # any i <= l。nums[i] <= nums[right]
            nums[l], nums[right] = nums[right], nums[l]

            if l - left + 1 == k:
                return nums[l]
            elif l - left + 1 < k:
                return quick(l+1, right, k - (l - left + 1))
                
            else:
                return quick(left, l-1, k)
        
        # 对于 偶数长度的区间，其中位数所在区间内任何值都是满足题意的最佳位置选项
        item = quick(0, n-1, (n+1)//2)
        ans = 0
        return sum(abs(item - i) for i in nums)


print(Solution().minMoves2([1,2,3]))