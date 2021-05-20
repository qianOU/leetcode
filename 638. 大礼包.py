class Solution:
    def shoppingOffers(self, price, special, needs) -> int:

        cost = float('inf')
        n = len(needs)
        special = [i for i in special if sum(i[idx]*price[idx] for idx in range(n)) >= i[-1]]
        
        from functools import lru_cache
        @lru_cache(None)
        def dfs(path, money):
            nonlocal cost
            if any(i<0 for i in path):
                return
            elif all(i==0 for i in path):
                cost = min(money, cost)
                return
            
            for item in special:
                k = min((path[i] // item[i]) for i in range(n) if item[i])
                for ii in range(1, k+1):
                    dfs(tuple((path[i] - ii*item[i]) for i in range(n)), money + ii*item[-1])
            
            path = list(path)
            for i in range(n):
                if path[i] == 0:
                    continue
                money += price[i] * path[i]
                path[i] = 0
            
            dfs(tuple(path), money)
        
        dfs(tuple(needs), 0)

        return cost

print(Solution().shoppingOffers([6,3],
[[3, 2, 9], [1, 2, 1], [2, 5, 9]],
[6,6]))