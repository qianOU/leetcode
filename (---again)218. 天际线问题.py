class Solution:
    # 线性扫描过程
    # 保持高度的有序：使用 堆 来保证  + 延迟删除策略，来较少堆在移除元素的过程中，线性的查询时间
    def getSkyline(self, buildings):
        n = len(buildings)
        tmps = []
        for l, r, h in buildings:
            tmps.append([l, -h]) 
            tmps.append([r, h])
        
        # 排序
        # 1. 优先处理横坐标靠前的节点
        # 2. 横坐标相同的时候优先处理 左端点
        # 3. 当都是左端点时，优先处理 高度 更大的端点 （执行入堆操作）
        # 4. 当都是右端点的时候，优先处理 高度 小的端点 （执行删除操作）
        tmps.sort(key = lambda x: (x[0], x[1]))

        import heapq
        heap = [0] # 小根堆，要转换为大根堆
        #tips: 要将右边界的0，也放入堆中作为保障

        prev = 0
        from collections import defaultdict
        delate = defaultdict(int) # 延迟删除字典
        ans = []
        for p, h in tmps:
            if h < 0: 
                heapq.heappush(heap, h)
            else:
                delate[-h] += 1
            
            # 延迟删除
            while True:
                if heap[0] in delate:
                    delate[heap[0]] -= 1
                    if delate[heap[0]] == 0:
                        del delate[heap[0]]
                else: break
                heapq.heappop(heap)
            
            cur = heap[0]
            if cur != prev:
                ans.append([p, -cur])
                prev = cur
        
        return ans