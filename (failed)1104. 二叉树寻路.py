class Solution:
    def pathInZigZagTree(self, label: int) :
        if label == 1:
            return [1]
        depth = len(str(bin(label))) - 3 # 节点位于的树的深度
        pair = 1 << (depth-1)
        ans = [1]
        h = 0
        total = 1
        while pair > 0:
            h += 1           
            total  = (total<<1) + ((pair & label)!=0)
            print(total, (pair & label))
            ans.append(2**(h+1)-1 - total + 2**h)

            pair >>= 1
            # print(h, flag==1, total, ans)
        return ans


print(Solution().pathInZigZagTree(14))