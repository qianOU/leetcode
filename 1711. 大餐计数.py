class Solution:
    # 字典树 还是 O（N2） 
    def countPairs(self, deliciousness) -> int:
        mod = 10**9 + 7

        from collections import defaultdict

        class Trie:
            def __init__(self):
                self.val = 0 # 记录出现的次数
                self.num = 0
                self.child = defaultdict(self.__class__)
            
            def insert(self, val):
                cur =  self
                for i in range(21):
                    cur = cur.child[(val >> i) & 1]
                cur.val += 1
                cur.num = val
                
 
            def search(self, val):
                cur  = self
                more = 0
                return self.dfs(val, cur, 0, 0)
 
            def dfs(self, val, cur, layer, more=0, bit_1=0):
            
                if not cur.child:
                    return cur.val if  bit_1 else 0
                    
                item = ((val >> layer) & 1) + more 
                ans = 0
                
                if item & 1:
                    bit_1 |= 1 

                    ans += self.dfs(val, cur.child[1], layer+1, 1, bit_1)
                    if  not (val >> layer + 1):
                        while cur.child.get(0):
                            cur = cur.child[0]
                        ans += cur.val

                elif item & 2:
                    bit_1 |= 1 
                    ans += self.dfs(val, cur.child[0], layer+1, 1, bit_1)

                else:
                    tmp = cur
                    if  not (val >> layer):
                        cur = cur.child[1]
                        while cur.child.get(0):
                            cur = cur.child[0]
                        ans += cur.val
                    
                    ans += self.dfs(val, tmp.child[0], layer+1, 0, bit_1)

                return ans
        

        trie = Trie()
        ans = 0
        for i, num in enumerate(deliciousness):
            if trie.child:
                item = trie.search(num)
                ans += item
                print(i, num, item)
            trie.insert(num)

        return ans % mod

   



print(Solution().countPairs([2160,1936,3,29,27,5,2503,1593,2,0,16,0,3860,28908,6,2,15,49,6246,1946,23,105,7996,196,0,2,55,457,5,3,924,7268,16,48,4,0,12,116,2628,1468]))