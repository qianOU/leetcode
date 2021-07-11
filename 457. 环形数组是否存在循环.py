class Solution:
    # 循环就是指针移动问题
    def circularArrayLoop(self, nums) -> bool:
        n = len(nums)
        # 辅助函数，对于 超出 索引 以及 前后移动 统一 转换为 [0, n-1] 之间
        correct = lambda x: x % n if x >= n else ( x if x >= 0 else  x % n  )
        # 走过的位置设为 特殊的标记符 tag
        for i in range(n):
            # 如果是已经遍历过的节点，则不再进行遍历
            if nums[i] > 1000: continue 
            prev = l = i
            sign = nums[i]
            tag = 2001 + i # 设置为特殊标志位，为了和 nums[i] 的数据范围区分开，每一轮探索都是唯一的
            # 当走的每一步都是同号， 并且是 未成走过的节点的时候
            while nums[l] * sign > 0 and nums[l] <= 1000:
                tmp = nums[l]
                nums[l] = tag # 将其设置为 tag， 表示已经探索过
                prev = l
                l = correct(l + tmp) # 指针移动到下一个位置
            
            if prev == l: # 如果是 长度为 1的循环，则继续探索
                continue
            # 如果循环长度大于1，则找到了循环
            elif nums[l] == tag: return True


        return False
