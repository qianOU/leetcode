class Solution:
    # 贪心 每次走的都是选择较多的那一步, 实质是维护 最远距离 
    # 写的不够优雅
    def canJump(self, nums) -> bool:
        n = len(nums)
        i = prev = 0
        while i < n-1:
            choices =  nums[i]
            if not choices: return False
            i += max(range(1, choices+1), key=lambda x:x + nums[i+x] if i+x <n else 0)
            if i == prev:
                return False
            prev = i
        
        return True
    
    # 优雅的写法: 维护当前能够到达的最远距离
    def canJump(self, nums) -> bool:
        n = len(nums)
        i = rightmost = 0
        while i <= rightmost:
            rightmost = max(nums[i]+i, rightmost) # 维护在i索引处，能走到的最远距离为 rightmost
            if rightmost >= n-1: return True
        
        return False
            
