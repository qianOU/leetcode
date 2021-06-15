class Solution:
    # 直接模拟交换的过程，超时！！
    def getLastMoment(self, n: int, left, right) -> int:
        import math
        time = 0
        while left or right:
            
            ruler = [0]*2*n
            for i in right:
                if i <= n-1:
                    ruler[2*i+1] = 1
            
            for j in left:
                if j>0:
                    ruler[2*j-1] += 10
            
            left, right = [], []
            for idx, i in enumerate(ruler):
                if i == 10:
                    left.append(idx//2)
                elif i == 1:
                    right.append((idx + 1)//2)
                elif i:
                    right.append((idx+1)//2)
                    left.append(idx//2)
            
            if left or right:
                time += 1
            print(left, right, ruler, time)
        
        return time

    #脑经急转弯， 由于交换方向没有成本，因此等价于没有交换
    def getLastMoment(self, n: int, left, right) -> int:
        ans = max(left) if left else 0
        for j in right:
            ans = max(ans, n-j)
        return ans
        
print(Solution().getLastMoment(
7,
[],
[0,1,2,3,4,5,6,7]
))