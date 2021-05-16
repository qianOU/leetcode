class Solution:
    # 基于特俗比较规则的 快排
    def largestNumber(self, nums: List[int]) -> str:
        res = [str(i) for i in nums]

        def quick(l, r): # 闭 闭
            if l > r:
                return 
            K = res[l]
            lo, ro = l+1, r

            while lo <= ro:
                while lo <= ro and res[lo] + K > K + res[lo]:
                    lo += 1
                while ro >= lo and K + res[ro] > res[ro] + K:
                    ro -= 1
                
                if lo >= ro:
                    break

                res[lo], res[ro] = res[ro], res[lo]
                lo, ro = lo+1, ro-1
            
            res[l], res[ro] = res[ro], res[l]

            quick(l, ro-1)
            quick(ro+1, r)
        
        quick(0, len(res)-1)
        ans = (''.join(res)).lstrip('0') # 去除前导0
        return ans if ans else '0'