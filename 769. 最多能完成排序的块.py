class Solution:
    # 我是控制了最大最小值， 实际上只需要控制最大值即可！！1
    def maxChunksToSorted(self, arr) -> int:
        count = 0
        max_, min_ = 0, 0
        flag = 0
        for idx, p in enumerate(arr):
            max_ = max(p, max_) #区间最大值

            if not flag and p == min_: # 找到下一个分块区间最小值
                flag = 1  # 设置标志位为找到最小值 
            
            if flag and max_ == idx: # 查看最大值是否匹配
                count += 1
                min_ = max_ + 1 # 其后下一个区间的最小值是本区间最大值 + 1
                flag = 0 

        return count
    
    # 从头开始遍历，只控制最大值
    def maxChunksToSorted(self, arr) -> int:
        count = num = 0
        for i, v in enumerate(arr):
            num = max(v, num)
            if i == num: count += 1
        return count