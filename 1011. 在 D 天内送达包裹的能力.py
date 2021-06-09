class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
       
        
        # 二分查找最小的 R, 也就是左边界
        l, r = max(weights), sum(weights)

        while l <= r:
            mid = l + (r-l) // 2
            
            cnt = 0
            cumsum = 0
            for i in weights:
                cumsum += i
                if cumsum > mid:
                    cumsum = i
                    cnt += 1
            
            cnt = cnt + 1 # 最后一步是一定要运输一次的， 但是如果超过了 mid 则还需要额外m天运输
            print(l, r, mid, cnt, cumsum)
            if cnt > days: l = mid + 1
            else: r = mid - 1
        
        return l

print(Solution().shipWithinDays( [1,2,3,1,1],
4))