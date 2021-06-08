class Solution:
    # 方法一： 基于值【小于等于i的数字个数】的二分查找 O(NlogN)
    # 事实是 重复的元素一定是第一个 cnt[i] > i 的元素
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) >> 1
            cnt = 0
            for i in range(n+1):
                cnt += nums[i] <= mid

            if cnt <= mid: l = mid + 1
            else:# 符合要求的出口
                r = mid - 1
        
        return l

# 为什么有重复元素的话一定有环存在呢？

# 我觉得可以这么理解：
# 1. 如果是完全不重复的元素，则按楼主给定的规则会形成一条路
# 2. 如果有重复元素，只不过是将那些本该出现的不重复元素替换了
# 3. 这样原本的路某些节点就会也指向重复元素，也就形成了环
    # Floyd 判圈算法 判断是否有环产生
    # 将每一个 nums[i] 看作是· i---> nums[i] 的一条边
    # 因为有重复元素，所以一定存在环
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0
        while not s or s!=f:
            s = nums[s]
            f = nums[nums[f]]
        
        s = 0
        while s!=f:
            s = nums[s]
            f = nums[f]
        
        return s
