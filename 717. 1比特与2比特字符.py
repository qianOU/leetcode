class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        p = 0
        n =len(bits)
        while p < n - 1:
            # if bits[p:p+2] in [[1,0], [1, 1]]: # 写的太冗余了
            if bits[p] == 1:
                p += 1
            p += 1
        # 太冗余了
        # if p != n:
        #     return True
        # return False
        return p == n-1

print(Solution().isOneBitCharacter([0,1,0]))