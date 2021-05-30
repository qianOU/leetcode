class Solution:
    # 思路1： 暴力法 有重复计算的问题
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        index = [i for i, j in enumerate(boxes) if j == '1']
        ans = []
        for i in range(n):
            ans.append(abs(i-j) for j in index)
        
        return ans
    
    # 思路2：前缀和 以及 后缀和
    def minOperations(self, boxes: str) -> List[int]:
        n = len(box)
        prefix, sufix = [0]*n, [0]*n
        presum = sufsum = 0
        count_pre = count_suf = 0

        for i in range(n):
            prefix[i] += presum
            count_pre += 1 if boxes[i] == '1' else 0
            presum += count_pre
        
        for i in range(n-1, -1, -1):
            sufix[i] = sufsum
            count_suf += 1 if boxes[i] == '1' else 0
            sufsum += count_suf
        
        return [i+j for i,j in zip(prefix, sufix)]
        
