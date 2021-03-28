class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_s = {'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
        "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        ans = 0
        right = 0
        while right < len(s):
            if s[right]  in ['I', 'X', 'C'] and (right+2) <= len(s) and map_s.get(s[right: right+2]) is not None:
                ans += map_s.get(s[right: right+2])
                print(right, s[right: right+2],map_s.get(s[right: right+2]))
                right += 2

            if right < len(s):
                if right+2<=len(s) and map_s.get(s[right: right+2]) is not None:
                    ans += map_s.get(s[right: right+2])
                    right += 2
                    continue
                ans += map_s.get(s[right])
                print(s[right],map_s.get(s[right]))
                right += 1
        
        return ans

    def romanToInt2(self, s):
            """
            :type s: str
            :rtype: int
            """
            map_s = {'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
            "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
            i = ans = 0    
            while i < len(s):
                if s[i:i+2] in map_s:
                    ans += map_s[s[i:i+2]]
                    i+=2
                else:
                    ans += map_s[s[i]]
                    i+=1
            
            return ans

    # 小的罗马数字在左边等效于减法 
    def romanToInt3(self, s):
            """
            :type s: str
            :rtype: int
            """
            map_s = {'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
            }
            ans = 0
            i = 0
            while i < len(s)-1:
                if map_s[s[i+1]]> map_s[s[i]]:
                    ans -= map_s[s[i]]
                else:
                    ans += map_s[s[i]]
                
                i+=1
            
            return ans + map_s[s[-1]]

A = Solution()
print(A.romanToInt3("MCMXCIV"))