class Solution:
    # 排序 + 双指针
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = float('inf')

        for i in range(n-1):
            total = nums[i]
            l, r = i+1, n-1
            while l < r:
                # 当前 三个元素的和
                item = total + nums[l] + nums[r] 
                ans = min([item, ans], key= lambda x: abs(x - target))
                
                if item > target:
                    # 将 r 移动到下一个不相同的元素处,节约时间
                    while r > l and nums[r-1] == nums[r]:
                        r -= 1
                    else: # 使用 else 表示不相等的时候移动一位
                        r -= 1        
                elif item < target:
                    # 将 l 移动到下一个不相同的元素处,节约时间
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    else: # 使用 else 表示不相等的时候移动一位
                        l += 1
                else:
                    return target

        return ans 

print(Solution().threeSumClosest(
[-1,2,1,-4],
1
))