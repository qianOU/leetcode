class Solution:
    # 贪心， 每次走到的都是最远处，不够简介，还是有部分元素被重复访问
    def jump(self, nums) -> int:
        n = len(nums)
        count = 0
        cur = pre = 0
        while cur < n-1:
            tmp = pre = cur # tmp 维护的是最远的位置索引， # cur 是当前所在的位置索引
            for j in range(1, nums[cur]+1):
                if pre + j >= n-1:
                    cur = pre + j
                elif pre + j + nums[pre + j] > tmp:
                    cur =  pre + j
                    tmp =  pre + j + nums[pre + j]
            
            count += 1      
        
        return count

    # 优化 : 1次遍历
    def jump(self, nums) -> int:
        n = len(nums)
        maxPos = now = end = step = 0
        while end < n-1:
            # 记录的是 [now，end] 位置处，能到达的最远距离 第 step 能走的最远距离
            maxPos = max(maxPos, now + nums[now]) # 更新能跳到的最远位置
            if now == end:
                step += 1
                end = maxPos # 第 step 能跳到的最远距离
                
            now += 1

        return step


print(Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0]))