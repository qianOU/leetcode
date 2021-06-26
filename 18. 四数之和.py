class Solution:
    # 三数和的变种
    # 实际上，还可以加入一些剪枝操作！！！减少运行时间
    # 剪枝操作十分重要！！！！
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n-3):
            # 剪枝1：
            if sum(nums[i:i+4]) > target:
                break
                
            # 剪枝2:
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue

            # 移动到不重复的元素处
            if i > 0 and nums[i-1] == nums[i]:
                continue

            for j in range(i+1, n-2):
                # 剪枝
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                # 剪枝
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue

                # 移动到不重复的元素处
                if j>i+1 and nums[j-1] == nums[j]:
                    continue

                l, r = j+1, n-1
                
                tmp = nums[i] + nums[j]
                while l < r:
                    total = tmp + nums[l] + nums[r] - target
                    # 如果和小于 target
                    if total < 0:
                        # 将 l 移动到下一个不相等的元素处
                        res = nums[l]
                        while l<r and nums[l] == res:
                            l += 1
                    
                    elif total > 0:
                        # 将 r 移动到下一个不相等的元素处
                        res = nums[r]
                        while l<r and nums[r] == res:
                            r -= 1
                    
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        # 将 l 移动到下一个不相等的元素处
                        res = nums[l]
                        while l<=r and nums[l] == res:
                            l += 1
                        # 将 r 移动到下一个不相等的元素处
                        res = nums[r]
                        while l<=r and nums[r] == res:
                            r -= 1
        
        return ans