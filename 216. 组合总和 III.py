class Solution:
    def combinationSum3(self, k: int, n: int):
        
        num2str = lambda x: ''.join(str(i) for i in x)
        ans = []
        visited = set()
        def back_track(k, n, path):
            if not k:
                if not n:
                    res = [i+1 for i in range(9) if path[i]]
                    ans.append(res)
                return 

            for i in range(1, 10):
                if n-i < 0 : return 
                if path[i-1]: continue

                path[i-1] += 1 # 做选择
                sign  =  num2str(path)
                if sign not in visited:
                    visited.add(sign)
                    
                    back_track(k-1, n-i, path)

                path[i-1] -= 1 # 回溯
            
        
        back_track(k, n, [0]*9)
        return ans

print(Solution().combinationSum3(3, 7))