class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        presum = [code[0]]

        n = len(code)
        for i in range(1, n):
            presum.append(code[i] + presum[-1])
        
        res = []
        if k>0:
            for i in range(n):
                if i + k < n:
                    res.append(presum[i+k] - presum[i])
                else:
                    res.append(presum[n-1]-presum[i] + presum[(i+k)%n])
        elif k < 0:
            for i in range(n):
                if i + k > 0:
                    res.append(presum[i-1] - presum[i+k-1])
                else:
                    item = presum[i-1] if i >= 1 else 0
                    res.append(item+presum[n-1] - presum[i+k-1])
        
        else:
            res = [0]*n
        
        return res