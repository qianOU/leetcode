class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        count = 0
        def fun(num):
            nonlocal count
            ans = []
            if (veganFriendly == 0 or num[2] == veganFriendly) and num[-2] <= maxPrice and num[-1] <= maxDistance:
                ans.append((num[1], num[0]))
                count += 1
            else:
                ans.append((-1,))
            
            return ans

        restaurants.sort(key=fun, reverse=True)

        return [i[0] for i in restaurants[:count]]