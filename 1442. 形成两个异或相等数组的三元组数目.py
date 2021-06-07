class Solution:
    def countTriplets(self, arr) -> int:
        # a^b = 0
        prexor = [0]
        for i in arr:
            prexor.append(i^prexor[-1])
        
        print(prexor)
        n = len(arr)
        count = 0
        for i in range(1, n):
            ans = prexor[i-1]
            for j in range(i+1, n+1):
                tmp = ans ^ prexor[j]
                if not tmp:
                    count += j-i

                print(i, j, tmp, count)
        return count


print(Solution().countTriplets([1,1,1,1,1]))