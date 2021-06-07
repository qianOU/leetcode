class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # 指针问题, 
        # step1 先找寻到按要求的最后一个元素位置，
        count = 0
        n = len(arr)
        for i in range(n):
            if not arr[i]:
                count += 1
            count += 1
            if count >= n: break
        
        
        # 双指针
        l = i # 这就是 复写后数组的最后一处索引
        r = n-1 # 数组末尾位置，其指针一定是不在 l 之前的
        
        if count > n:  # 特殊情况，如果受限于长度，最后只能复写一个0的情况
            arr[r] = 0
            r -= 1
            l -= 1

        while l >= 0:
            if not arr[l]:
                arr[r] = 0
                arr[r-1] = 0
                r = r - 2
                l -= 1
            else:
                arr[r] = arr[l]
                r, l = r-1, l-1