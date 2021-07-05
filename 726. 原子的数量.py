class Solution:
    # 使用递归来处理
    def countOfAtoms(self, formula: str) -> str:

        formula += '*' # 追加特殊字符，便于处理最后的子公式逻辑不被遗忘，即最后一个字符不为 ） 的时候，也能正确处理
        n = len(formula)
        from collections import defaultdict
        
        # 处理 formula[start:] 的原子统计结果
        #  返回 处理完 某个子公式，返回 下一个子公式的指针，以及嵌套统计结果
        def helper(start):
        
            stack = []
            p = start
            beg = '' # 记录原子
            res = 1 # 记录原子个数
            
            while p < n:
                if formula[p].isdigit():
                    res = 0
                    while p < n and formula[p].isdigit():
                        res = res*10 + ord(formula[p])  - ord('0')
                        p += 1
                    res = max(res, 1)
                    
                else:
                    # print(beg, res, p, formula[p])
                    if beg and res:
                        stack.append([beg, res])
                    beg, res = '', 1 # 设置为 某个 原子的 默认状态 
                    
                    # 遇见左括号进行迭代
                    if formula[p] == '(':
                        cur, items = helper(p + 1)
                        stack.extend(items)
                        p = cur # 将 p 指向 下一个公式，进行下次搜索
                        continue
                    
                    # 遇见右括号 迭代 结束
                    elif formula[p] == ')':
                        p += 1
                        res = 0
                        while p < n and formula[p].isdigit():
                            res = res*10 + ord(formula[p]) - ord('0')
                            p += 1
                        
                        # 进行倍数扩征
                        if res:
                            for i in stack:
                                i[1] *= res
                        
                        break
                        # return (p, stack)
                    
                    # 如果是 字符
                    elif formula[p].isalpha():
                        beg = formula[p]
                        while p + 1 < n and formula[p+1].isalpha() and formula[p+1].islower():
                            beg += formula[p + 1]
                            p += 1

                    # p 指针移动到下一位 
                    p += 1

            
            return p, stack
        
        _, stack = helper(0)

        # 将 原子统计 结果 综合为 一个 表
        dic = defaultdict(int)
        for item in stack:
            dic[item[0]] += item[1]
        
        # 对表按 字典序进行排序
        ans  = ''
        for i in sorted(dic):
            ans += i
            if dic[i] > 1:
                ans += str(dic[i])
        
        return ans

    # 使用栈来处理，栈每次push的是每一层的统计结果
    # 所以栈的长度也就表明了当前处于化学式的深度
    def countOfAtoms(self, formula: str) -> str:
        from collections import defaultdict
        stack = [defaultdict(int)]

        l = 0
        n = len(formula)
        while l < n:
            if formula[l] == '(': # 深度 + 1
                stack.append(defaultdict(int))
                l += 1
            elif formula[l] == ')': # 深度 - 1， 合并结果
                # 查看后面的数字
                res = 0
                l += 1
                while l < n and formula[l].isdigit():
                    res = res*10 + ord(formula[l]) - ord('0')
                    l += 1
                
                # 合并到上一层
                res = max(res, 1)
                drop = stack.pop() # 待合并的 子化学式
                for i in drop:
                    stack[-1][i] += res*drop[i] 

            elif formula[l].isalpha(): # 对于 一个 原子 进行统计
                beg = formula[l]
                l += 1
                # 找寻原子的化学式
                while l < n and formula[l].isalpha() and formula[l].islower():
                    beg += formula[l]
                    l += 1
                # 统计该原子在这一层出现的次数
                res = 0
                while l < n and formula[l].isdigit():
                    res = res*10 + ord(formula[l]) - ord('0')
                    l += 1
                
                res = max(res, 1)
                stack[-1][beg] = res # 记录在当层的 字典 中

        dic = stack[0]
        print(dic)
        # 对表按 字典序进行排序
        ans  = ''
        for i in sorted(dic):
            ans += i
            if dic[i] > 1:
                ans += str(dic[i])
        
        return ans


a = "((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"
print(Solution().countOfAtoms(a))