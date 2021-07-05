class Solution:
    # 二分 wrong！！！！！
    def search(self, nums, target: int) -> bool:
        import time
        l, r = 0, len(nums) # 左闭右开区间
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if target < nums[mid] <= nums[-1]:
                r = mid
            elif nums[mid] < target <= nums[-1]:
                l = mid + 1
            elif nums[mid] > target >= nums[0]:
                r = mid
            elif target > nums[mid] >= nums[0]:
                l = mid + 1
            else:
                # 如果 nums[mid] 
                # time.sleep(.2)
                # print(nums[mid], target, l ,r)
                break
        
        return False

class Solution:
    # 二分， 需要考虑 mid 落在区间的 左部分还是右部分
    def search(self, nums, target: int) -> bool:
        import time
        l, r = 0, len(nums) # 左闭右开区间

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            # 有重复的元素的时候，需要加入这一个判断条件
            if nums[l] == nums[mid] == nums[r-1]: # 如果 nums[mid] 与 左右区间的阈值相等，这就无法确认 mid 落在哪个有序区间
                l += 1
                r -= 1 # 同时缩小 左右边界
            # 如果 mid 在右半部分区间
            elif nums[mid] <= nums[r-1]:
                # 如果落在右半部分的有序区间中的时候
                if  nums[mid] < target <= nums[r-1]:
                    l = mid + 1
                else: # target 落在 mid 的左侧，这就不一定是有序区间了
                    r = mid
            # 如果 mid 在左半部分区间
            elif nums[mid] >= nums[l]:
                # 如果落在左半部分的有序区间中的时候
                if  nums[mid] > target  >= nums[l]:
                    r = mid
                else: # target 落在 mid 的右侧，这就不一定是有序区间了
                    l = mid + 1
            else: 
                break

        return False