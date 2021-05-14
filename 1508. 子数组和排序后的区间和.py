class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        n = len(nums)
        def get(k, ans=[]):
            if k == n-1:   
                ans.append(nums[k])
                return [nums[k]]
            
            res  = get(k+1, ans)
            tmp = [nums[k]]
            tmp.extend([nums[k] + i for i in res])
            ans.extend(tmp)
            return tmp

        
        answ = []
        sorted(get(0, answ))
        return sum(sorted(answ)[left-1:right]) % (10**9 + 7)