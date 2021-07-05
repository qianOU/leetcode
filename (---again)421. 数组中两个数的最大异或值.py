class Solution:
    # 字典树：实际存的是就是数字，不过是以二进制的形式存储的
    def findMaximumXOR(self, nums: List[int]) -> int:

        
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(self.__class__)

        class Trie:
            def __init__(self, nums):
                # 根节点
                self.root  = TrieNode()
                # 使用
                for n in nums:
                   self.insert(n)

            def insert(self, v):
                cur = self.root
                for i in range(31, -1, -1): # 树的层次是 二进制的高位 ---> 二进制的低位
                    item = (v >> i) & 1
                    cur = cur.children[item]
            
            # 找寻和 m 异或 最大的元素
            def search(self, m):
                res, cur = 0, self.root # res 记录的是 字典树搜索的过程，将二进制恢复为 整数
                for i in range(31, -1, -1):
                    item = (m >> i) & 1
                    if 1-item in cur.children:
                        res += (1<<i)
                        cur = cur.children[1-item]
                    else: # 如果 不存在 i 的位置可以异或为 1 的，就查看其低位是否会存在异或为 1的情况
                        cur = cur.children[item]

                return res
        
        trie = Trie(nums)
        return max(trie.search(i) for i in nums)


                        



