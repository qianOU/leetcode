class Solution:
    # 二分查找
    # 确定 二分查找的磁力的取值范围为 [1, （right_bound - left_bound）//(m-1)]
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        # 检查 以 length 作为 最小磁力时，是否可以容纳得下 n 个节点
        def check(length):
            count = 1 # 首先将最左端的端点放上一个元素
            j = 0
            for i in range(len(position)):
                if position[i] - position[j] >= length:
                     count += 1
                     j = i
                     if count >= m: return True
        
        left = 1
        right = (position[-1] - position[0])//(m-1)
        
        # 因为要求最大话 最小磁力距离， 也就是 最小磁力距离的右边界
        while left <= right:
            mid = left + (right-left)//2
            # 如果以 mid 作为最小磁力距离，时有 大于等于 m 个 点可以满足，则加大最小磁力距离，即收缩左边界
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
