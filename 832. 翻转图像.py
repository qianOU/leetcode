class Solution:
    def flipAndInvertImage(self, image):
        m, n = len(image), len(image[0])
        mat = []

        encode = lambda list_a: sum(j<<i for i, j in enumerate(list_a))
        decode = lambda x: [(x>>(n-1-i))&1 for i in range(n)]
        tmp = (1<<n) - 1
        print(tmp)
        for i in range(m):
            code = encode(image[i])
            print(code)
            mat.append(decode(code^tmp))
        
        return mat

print(Solution().flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))