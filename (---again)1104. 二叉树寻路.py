class Solution:
    def pathInZigZagTree(self, label: int) :
        if label == 1:
            return [1]
        d = len(bin(label)[2:]) - 1
        ans = [label]
        while label > 1:
            total = (2**(d)-1 + 2**(d-1))
            ans.append(total - label//2)
            label = ans[-1]
            d = d - 1
        
        return ans[::-1]

        

print(Solution().pathInZigZagTree(14))