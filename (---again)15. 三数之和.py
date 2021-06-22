class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans =  []
        n = len(nums)

        # 先固定 i
        for i in range(n-2):
            # 下一个第一个元素，移动到不相等的下一个元素上
            if i > 0 and nums[i-1] == nums[i]:
                continue
            # 双指针
            l, r = i+1, n-1
            # 使用左右指针 利用有序性，搜寻 其它 两个元素
            while l < r:
                item = nums[i] + nums[l] + nums[r]

                if item > 0:
                    # item 比较大，所以需要将 右指针，移动到下一个不相同的元素
                    tmp = nums[r]
                    while l<r and nums[r-1] == nums[r]:
                        r -= 1
                    if nums[r] == tmp: r-=1
                    

                elif item < 0:
                    tmp = nums[l]
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    if tmp == nums[l]: l+=1
                        
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # 左指针移动到下一个不相等的元素之上
                    tmp = nums[l]
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    if tmp == nums[l]: l+=1
                    # 右指针移动到下一个不相等的元素之上
                    tmp = nums[r]
                    while l<r and nums[r-1] == nums[r]:
                        r -= 1
                    if tmp == nums[l]: r-=1
        
        return ans

print(Solution().threeSum([-1,0,1,2,-1,-4]))