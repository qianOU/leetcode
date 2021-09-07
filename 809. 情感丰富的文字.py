class Solution:
    # 指针数组问题
    def expressiveWords(self, s: str, words) -> int:
        m, n = len(s), len(words)
        points = [0]*n
        length = list(map(len, words))
        l = 0 
        for r in range(m+1):
            if r < m and s[r] == s[l]: continue
            else:
                count = r - l
                for i in range(n):
                    
                    if points[i] < 0 or points[i] >= length[i] or words[i][points[i]] != s[l]: 
                        points[i] = -1
                        continue
                    
                    if count >= 3:
                        res = count
                        while res > 0 and points[i] < length[i] and words[i][points[i]] == s[l]:
                            points[i] += 1
                            res -= 1

                    elif words[i][points[i]: points[i]+count] == s[l:r]:
                        points[i] += count
                    else:
                        points[i] = -1
                        
                l = r

        return sum(i == j for i, j in zip(points, length))

print(Solution().expressiveWords("zzzzzyyyyy",
["zzyy","zy","zyy"]))