class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        

        def back_track(i, path):
            nonlocal count
            if i == n+1:
                count += 1
                return
            
            # 做选择
            for j in range(1, n+1):
                if j in path:
                    continue
                
                if j%i==0 or i%j==0:
                    path.append(j)
                    back_track(i+1, path)
                    path.pop()
        
        back_track(1, [0])

        return count
                

print(Solution().countArrangement(3))