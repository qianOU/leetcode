class Solution:
    # 滚动队列窗口 超时了 
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        
        def check(window):
            n = len(window)
            return any(abs(window[i] - window[i-1])<=t for i in range(1, n))



        window = sorted(list(nums[:k+1]))
        p = 0
        first = True
        while p < n:
            right = p+k 
            if window and check(window):
                    return True
            window.remove(nums[p])
            y = nums[right + 1] if right < n-1 else None
            p += 1

            if y is not None:
                # 插入排序
                for idx, j in enumerate(window):
                    if j > y:
                        window = [*window[:idx], y, *window[idx:]]
                        break
            
                # 比任何值都大
                if not window or window[-1] <= y:
                    window.append(y)
            
        return False

    # 方法 1： 有序列表 + 二分查找
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        from sortedcontainers import SortedList # 有序列表 O（Nlog(k)）
        window = SortedList()

        import bisect

        n = len(nums)
        for i in range(n):
            if i > k:
                window.remove(nums[i-k-1])
            window.add(nums[i])
        # 找到 nums[i] 的索引处
        idx = bisect.bisect_left(window, nums[i])
        # 查看 nums[i] 的左右两侧是否有符合题意的解
        if idx > 0 and window[idx] - window[idx-1] <= t:
            return True
        if idx < n-1 and window[idx+1] - window[idx] <= t:
            return True
        
        return False


    # 方法 2： 桶排序
    # 有一个点： python 的取整总是向下取整的 无论正反
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        size = t + 1 # 桶的大小， [i,...j] 符合 abs(j-i) <= t时，集合上面有 t + 1 个元素
        map_ = {} # k 个桶的集合
        n = len(nums)

        # 值到桶的映射关系
        getindex = lambda u: u // size

        for ind, i in enumerate(nums):
            idx = getindex(i)
            if idx in map_:
                return True

            map_[idx] = i

            if idx - 1 in map_ and abs(i - map_[idx-1]) <= t:
                return True
            
            if idx + 1 in map_ and abs(i - map_[idx+1]) <= t:
                return True
            
            # 只保留k个组
            if ind >= k:
                map_.pop(getindex(nums[ind - k]))

        return False
