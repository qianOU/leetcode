class Solution:
    # 方法一： 基于优先队列
    def kClosest(self, points, k: int) :
        import queue
        q = queue.PriorityQueue()
    
        for idx, i in enumerate(points):
            dist = i[0]**2 + i[1]**2
            item = (dist, idx)
            q.put(item)
        
        ans = []
        for i in range(k):
            _, item = q.get()
            ans.append(points[item])
        
        return ans
    
    # 方法2 ： 排序 （手写快排） nlogn
    def kClosest(self, points, k: int):

        def quick(left, right, k): # 左闭右开
            if left >= right:
                return 
            
            K = points[left][0]**2 + points[left][1]**2
            l = left + 1
            r = right - 1

            while l <= r: # 左闭右闭的搜索区间
                while l < right and points[l][0]**2 + points[l][1]**2 < K:
                    l += 1
                while r >= 0 and points[r][0]**2 + points[r][1]**2 > K:
                    r -= 1  

                if l >= r:
                    break
                
                points[l], points[r] = points[r], points[l]
                l += 1
                r -= 1

            # 确保 [r, right) 都是 大于等于 K的            
            points[left], points[r] = points[r], points[left]

            
            # 检验 [left, r] 是否符合规定
            if r - left + 1 == k:
                return 
            
            elif r - left + 1 > k: # 在左半部分继续寻找
                quick(left, r, k)
            
            else: # 左半部已经部分符合要求，只要 右半部部分符合即可
                quick(r+1, right, k-(r - left + 1))
            
        quick(0, len(points), k)

        return points[:k]

    # 方法3 ： 快排 单支快排 o(n)
    def kClosest(self, points, k: int): # 左闭右闭的区间
        import random
        def random_quick(left, right, k):
            if left > right:
                return

            idx = random.randint(left, right)
            K = points[idx][0]**2 + points[idx][1]**2
            points[idx], points[right] = points[right], points[idx] # 讲基于交换到 最后一个位置，便于后序的交换位置
            i = left - 1
            for j in range(left, right):
                if  points[j][0]**2 + points[j][1]**2 <= K: # 如果是小于等于k的，则需要将[left, i] 的区间变大
                    i += 1
                    points[i], points[j] = points[j], points[i]
            

            # 最后是 [left, i] 是小于等于 k的， [i+1, right) 是大于 k 的
            i += 1
            points[i], points[right] = points[right], points[i]

            # 检验 [left, r] 是否符合规定
            if i - left + 1 == k:
                return 
            
            elif i - left + 1 > k: # 在左半部分继续寻找
                random_quick(left, i-1, k)
            
            else: # 左半部已经部分符合要求，只要 右半部部分符合即可
                random_quick(i+1, right, k-(i - left + 1))

        random_quick(0, len(points)-1, k)

        return points[:k]



print(Solution().kClosest(
[[3,3],[5,-1],[-2,4],[-2,4],[-2,4],[-2,4]],
2))