class Solution:
    # 思路1: BFS(超时)
    def reachNumber(self, target: int) -> int:
        from collections import deque
        q = deque([0])
        
        visited = set([0])
        step = 0
        while q:
            sz = len(q)
            step += 1
            for _ in range(sz):
                cur = q.popleft()
                if cur == target:
                    return step - 1
                q.append(cur+step)
                q.append(cur-step)
        
    # 思路2: 二分查找（数据规模巨大。必然是logn的方法），转化为正数和负数的和角度来看
    def reachNumber(self, target: int) -> int:
        target = abs(target) # 正反是一致的
        l, r = 0, abs(target)
        while l <= r: # 找寻 第一个使得 cur >= 0 的 mid
            mid = (l + r) // 2
            cur = (mid**2 + mid) // 2 - target
            if cur < 0: l = mid + 1
            else: r = mid - 1
        cur = (l**2 + l) // 2 - target
        # 必须确保 cur 是偶数
        while cur % 2:
            cur += l + 1
            l += 1
        return l