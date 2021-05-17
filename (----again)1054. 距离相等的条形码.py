class Solution:
    def rearrangeBarcodes(self, barcodes):
        from collections import  Counter
        from queue import PriorityQueue as PQ

        counts = Counter(barcodes).most_common()
        q = PQ()
        for i in counts:
            q.put((-i[1], i[0]))

        ans = []
        while not q.empty():
            count1, one = q.get()
            if q.empty(): # 由于题目假设存在答案 ，所以不需要再做细致的判断
                ans.append(one)
                break
            count2, two = q.get()
    
            ans.extend([one, two]) # 每次穿插两个计数最多的字符
            if -count1 - 1 > 0:
                q.put((count1+1, one))
            if -count2 - 1 > 0:
                q.put((count2+1,two ))
                
        
        return ans

print(Solution().rearrangeBarcodes([7,7,7,8,5,7,5,5,5,8]))          



