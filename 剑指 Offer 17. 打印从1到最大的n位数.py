class Solution:
    def printNumbers(self, n: int) :
        res = []
        tmp = ['0']*n
        start = n-1
        while True:
            for i in range(1, 10):
                tmp[n-1] = str(i)
                res.append(int(''.join(tmp[max(start, 0):])))
        
            l = n-2
            if l < 0: return res
            while l >= 0:
                if any(i!='9' for i in tmp):
                    tmp[l+1] = '0'
                    if tmp[l] != '9':
                        tmp[l] = str(int(tmp[l]) + 1)
                        break
                    elif l == 0:
                        break

                    tmp[l] = '0'
                    l -= 1    
                else:
                    return res

            # 开始的索引
            start = max(0, min(l, start))
            res.append(int(''.join(tmp[max(start, 0):])))
            
        return res  

        

print(Solution().printNumbers(3), len(Solution().printNumbers(3)))