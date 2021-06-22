class Solution:
    def minDominoRotations(self, tops, bottoms) -> int:
        n = len(tops)
        records = [[0]*7 for i in range(2)]
        common = [tops[0], bottoms[0]]

        for i, j in zip(tops, bottoms):
            if i not in common and j not in common:
                return -1
            elif i in common and j  in common:
                if i!=j:
                    records[0][i] += 1
                    records[1][j] += 1
                else:
                    common = [i]

            elif i in common:
                records[0][i] += 1
                common = [i]
            else:
                records[1][j] += 1
                common = [j]
        
        print(common)
        ans = n
        for i in common:
            ans = min(records[0][i], records[1][i], ans)
    
        return ans


print(Solution().minDominoRotations(
[1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,1,1,1,1,1,2,1,2,2,1,1,2,2,2,2,2,1,1,2,2,2,2,1,2,1,1,2,1,1,1,1,2,1,2,2,2,1,2,1,2,2,1,2,1,2],
[2,1,1,1,2,1,2,1,2,2,1,1,1,2,1,2,2,1,2,2,2,1,2,2,1,1,1,2,1,2,2,1,2,1,1,2,1,1,1,2,1,2,2,2,2,1,2,1,1,2,1,2,2,1,2,1,1,2,2,1,2,1,1,2]
))