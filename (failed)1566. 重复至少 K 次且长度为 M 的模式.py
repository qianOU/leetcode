class Solution:
    def containsPattern(self, arr, m: int, k: int) -> bool:
        n = len(arr)
        l = 0
        f = m
        count = 1


        while f < n:
            tmp = f
            for p in range(l, l+m):
                if p<n and tmp<n and arr[p] == arr[tmp]:
                    tmp += 1
            print(l,  f, tmp, count)
            if tmp - f == m:
                count += 1
                if count >= k: 
                    # print(f, tmp, m, count)
                    return True
                f = tmp

            else: 
                count = 1
                f += 1
                l += 1
              
        
        return False

            

# print(Solution().containsPattern([5,6,2,6,6,3,3,3,3,1,1,
# 2,3,2,3,6,3,2,3,3,6,2,5,4,2,1,3,5,3,5,3,5,3,3,4,2,6,4,4,3,3,2,3,6,6,6,6,5,1,6,2,1,3,2,5,3,6,5,2,5,5,5,4,1,1]
# ,1
# ,5))

print(Solution().containsPattern(
[2,1,1,2,2,1,2,2,1,2],
1,
3
))