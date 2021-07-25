class Solution:
    # 【抽象成三指针问题】
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        def add(s1, s2):
            p1, p2 = len(s1) - 1, len(s2) - 1
            ans = ''
            more = 0
            while p1 >= 0 or p2 >= 0 or more:
                item1 = int(s1[p1]) if p1 >= 0 else 0
                item2 = int(s2[p2]) if p2 >= 0 else 0
                more, cur = divmod(item1 + item2 + more, 10)
                ans += str(cur)
                p1, p2 = p1 - 1, p2 - 1

            return ans[::-1]


        def check(i, j, k): # 三个指针，分别指向 1，2，3 数的起始位置
            # 查看是否有前导 0
            if (num[i] == '0' and j - i > 1) or (num[j] == '0' and k - j > 1): return False 
            elif k == n: return True

            res = add(num[i:j], num[j:k])
            m = len(res)
            if res == num[k: k+m]:
                return check(j, k, k+m)
            return False
        

        # 遍历最开始的三指针位置
        i = 0
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if check(i, j, k):
                    return True
        
        return False