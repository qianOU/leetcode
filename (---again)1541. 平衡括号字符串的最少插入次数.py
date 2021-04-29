class Solution:
    # 使用计数法，只要记录 （ 即可
    def minInsertions(self, s: str) -> int:
        insert = count = index = 0 # count 是 （ 的计数
        while index < len(s):
            if s[index] == '(':
                count += 1
            else:
                if not count: # 如果没有左括号了，需要插入一个左括号
                    count += 1
                    insert += 1 # 插入操作数 + 1
                if index < len(s) - 1 and s[index + 1] == ')': # 如果 连着两个都是 ）
                    count -= 1 # 抵消了一个左括号
                    index += 1 # 多移动一位
                else:
                    count -= 1 # 否则的化需要插入 一个 ）
                    insert += 1 #插入数 + 1
                    
            
            index += 1 

        return insert + 2*count # 插入数 以及 剩下的左括号 都需要插入两个 ） 进行匹配
                

print(Solution().minInsertions("(((()(()((())))(((()())))()())))(((()(()()((()()))"))




# print(Solution().minInsertions("(()))(()))()())))"))

