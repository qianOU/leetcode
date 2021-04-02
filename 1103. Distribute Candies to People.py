class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        n = num_people # 确定数组大效
        ans = [0]*n
        # i = round_ = 0
        i = 0
        while candies>0:
            index = i%n
            # if i>=n and i %n == 0:
            #     round_ += 1
            temp = i+1
            # temp = round_ * n + index + 1
            if candies <= temp:
                temp = candies
            ans[index] += temp
            candies -= temp
            i+=1
        return ans

print(Solution().distributeCandies(10 ,3))