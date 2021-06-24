class Solution:
    # 计数法 写的不够简洁！！！ 理论上 没有使用排序，效率应该更高，但实际不是。
    # 主要原因是：如果nums 中有些区间间隔很大，则我们需要遍历大间隔，这就可能导致比排序时间长了
    def isPossibleDivide(self, nums, k: int) -> bool:
        n = len(nums)
        if n % k: return False

        from collections import Counter
        a = Counter(nums)
        minx, maxx = min(a), max(a) # 找到最大最小值
        
        cur = minx
        prev = a[minx]
        while cur <= maxx:
            if a[cur] is None:
                return False
            # 将每轮不合理的数字先过滤掉
            while a[cur] == 0:
                cur += 1
            # 每一轮首元素的次数
            last = a[cur]
            prev = a[cur]
            tmp = None # 记录的是 k 个元素，首次次数大于 首元素的 位置
            
            for i in range(k):
                if a[cur] is None or prev > a[cur]:
                    return False
                if  tmp is None and a[cur] > prev:
                    tmp = cur

                prev = a[cur]
                a[cur] -= last # k 范围内的每个数都减去首元素次数
                cur += 1

            cur = tmp if tmp is not None else cur # 查看是否需要回退到某个位置
            

        return True
    
    # 排序 + 计数（对于区间间隔大而已，有性年优势）
    def isPossibleDivide(self, nums, k: int) -> bool:
        n = len(nums)
        if n % k: return False

        from collections import Counter
        a = Counter(nums)

        nums = sorted(a.keys())
        # 每次只争对区间的首元素进行查找
        for item in  nums:
            if a[item] > 0:
                # 确定 k 区间是否符合要求
                for j in range(item+1, item+k):
                    if a.get(j, 0) < a[item]:
                        return False
                    a[j] -= a[item]
        
        return True