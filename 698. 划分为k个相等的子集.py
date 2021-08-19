class Solution:
    # k 等分问题
    # 双指针问题
    # 贪心 每次都优先拿大的,不行弹出次小的,选择左指针元素
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        target, res = divmod(sum(nums), k)
        if res != 0: return False #不能被整除
        nums.sort()
        l, r = 0, len(nums)-1
        
        print(nums, target)
        stack = [] # 保存
        tmp = 0
        while l <= r:
            # print(l, r, tmp, stack)
            while l<=r and stack and tmp > target:
                r = stack.pop()
                tmp -= nums[r]
                tmp += nums[l]
                l += 1

            if tmp == target: 
                k -= 1
                tmp = 0
                print(l, r, tmp)
                stack.clear()

            stack.append(r)
            tmp += nums[r]
            r -= 1
        
        return tmp == target


print(Solution().canPartitionKSubsets(
[4,4,6,2,3,8,10,2,10,7],
4))