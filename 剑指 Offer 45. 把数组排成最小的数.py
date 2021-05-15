class Solution:
    # 基于特殊的比较规则的 快排序
    def minNumber(self, nums: List[int]) -> str:
        # 快排
        def quick(left, right, ans): # 闭，闭
            if left > right:
                return 

            k = ans[left]
            l = left + 1
            r = right
            while l <= r:
                while l<=right and ans[l] + k < k + ans[l]:
                    l += 1 
                while r>=0 and k + ans[r] < ans[r] + k:
                    r -= 1
                
                if l >= r:
                    break
                
                ans[l], ans[r] = ans[r], ans[l]
                l, r = l+1, r-1
            
            ans[left], ans[r] = ans[r], ans[left]

            quick(left, r-1, ans)
            quick(r+1, right, ans)


        from collections import defaultdict
        records = defaultdict(list)
        for i in nums:
            c = str(i)
            records[c[0]].append(c)
        

        # print(records)
        res = []
        for i in range(10):
            ans = records[str(i)]
            # print(i, ans)
            if not ans:
                continue
            quick(0, len(ans)-1, ans)
            res.extend(ans)
        
        return ''.join(res)