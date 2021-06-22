class Solution:
    # 方法一： 优先找寻 分割点，找到target是落于分割点的左部分还是右部分再确认
    def search(self, nums, target: int) -> int:
        # 找到分割点
        n = len(nums)
        l = 0
        r = n-1
        ans = n
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] >= nums[0]:
                l = mid + 1
            elif nums[mid] <= nums[-1]:
                if mid<=0 or  nums[mid-1] > nums[mid]:
                    ans = mid
                    break
                r = mid - 1
        
        print(ans)
        # ans 是最小的元素位置
        if target >= nums[0]:
            l, r = 0, ans-1 # 当nums 只有一个元素的时候，ans = 0这时需要特殊处理
            # 后半部分较小的元素长度
            # back = 0
        else:
            l, r = ans, n-1
           
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        
        return - 1
    
    # 方法2: 不需要找到分割点，直接在二分搜索的时候根据mid的值和 nums[0] 以及 nums[-1] 的大小关系来确认哪部分有序
    def search(self, nums, target: int) -> int:
        if not nums: return -1
        l, r = 0, len(nums)-1
        n = len(nums)-1
        while l <= r:
            mid = (l + r)//2
            print(l ,r)
            if nums[mid] == target: return mid
            # 如果在左半部，
            elif nums[mid] >= nums[l]:
                # 左半部分有序的情况下
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 如果在右半部有序的情况
            elif nums[mid] <= nums[r]:
                # 右半部分有序
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
        

        
print(Solution().search(
[5,1,3],
5
))