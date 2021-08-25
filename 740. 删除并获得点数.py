class Solution:
    # 优先队列
    def deleteAndEarn(self, nums) -> int:
        from collections import Counter
        from queue import PriorityQueue

        record = Counter(nums)
        print(record)
        q = PriorityQueue()
        for i in record:
            q.put((-i*record[i], i))
        ans = 0
        next = []
        while next or not q.empty():
            if next and q.empty():
                for _ in range(len(next)):
                    q.put(next.pop())
            

            total, item = q.get()   
            print(item, total, record)
            if item not in record: continue
            elif total <= -(item+1)*record[item+1] - (item-1)*record[item-1]:
                ans -= total
                del record[item + 1], record[item - 1], record[item]
                for _ in range(len(next)):
                    q.put(next.pop())
            else:
                next.append((total, item))
        return ans

        
            
print(Solution().deleteAndEarn([8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]))