class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps) -> int:
        
        n = len(source)
        hingtong = n
        visited = set()
        visited.add(tuple(source))

        def dfs(cur):
            print(cur)
            nonlocal hingtong

            hingtong = min(hingtong, sum(1 if cur[i]!=target[i] else 0 for i in range(n)))
            
             
            swap_times = 0
            tmp = cur.copy()
            for i, j in allowedSwaps:
                cur = tmp
                cur[i], cur[j] = cur[j], cur[i]
                if tuple(cur) not in visited:
                    visited.add(tuple(cur))
                    swap_times += 1
                    dfs(cur)
        

        
        dfs(source)

        return hingtong
            



print(Solution().minimumHammingDistance(
[41,37,51,100,25,33,90,49,65,87,11,18,15,18],
[41,92,69,75,29,13,53,21,17,81,33,19,33,32],
[[0,11],[5,9],[6,9],[5,7],[8,13],[3,13]]))
            
