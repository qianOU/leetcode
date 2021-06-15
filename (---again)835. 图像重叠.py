class Solution:
    # 算法思路：记录 图像 1 的索引位置，
    # 记录将 a 移动到 b 的时候， 其它位置也是偏移同等的单位，记录覆盖的最大量
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        A = [complex(i, j) for i, row in enumerate(img1)
                            for j, v in enumerate(row) if v]
        B =  [complex(i, j) for i, row in enumerate(img2)
                            for j, v in enumerate(row) if v]
        
        B2 = set(B)
        seen = set() # 去重，使用的是偏移量，因为便宜量一致的话，覆盖的1一定是一样多的
        ans = 0

        for i in A:
            for j in B:
                pix = i - j
                if pix not in seen:
                    seen.add(pix)
                    ans = max(ans, sum(i in B2 for i in A))

        return ans