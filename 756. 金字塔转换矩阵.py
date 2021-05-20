class Solution:
    def pyramidTransition(self, bottom: str, allowed) -> bool:
        n = len(allowed)

        from collections import defaultdict

        records = {}
        for i in allowed:
            records[i[:2]] = i[-1]


        all_path = []

        # 获取 string 所有可能的组合
        def fun(botton, start, path):
            n = len(botton)
            if start == n:
                all_path.append(path)
                return True
            # 不合规的
            elif start > n:
                return
            if not start:
                if not records.get(botton[:2], None):
                    return 
                return fun(botton, 2, path+records.get(botton[:2]))
                 
            # 选择 1   共用的情况         
            if records.get(botton[start-1:start+1], None):
                records[botton[start-1:start+1]] = ''
                tmp = records.get(botton[start-1:start+1])
                flag1 = fun(botton, start+1, path + tmp)
                records[botton[start-1:start+1]] = tmp
            # 选择 2 孤立的情况
            if records.get(botton[start:start+2], None):
                records[botton[start:start+2]] = ''
                tmp = records.get(botton[start:start+2])
                flag2 = fun(botton, start+2, path + tmp)
                records[botton[start:start+2]] = tmp        

            if flag1 or flag2:
                return 1

        def dfs(cur):
            if  len(cur) == 1:
                return True
            
            n = len(cur)
            # 得到所有可能的上层字符串
            a = fun(cur, 0, '')
            print(a, all_path)
            for item in all_path:
                if dfs(item):
                    return True
            
            # 清空 all_path
            all_path.clear()


        return bool(dfs(bottom))

print(Solution().pyramidTransition("AABA",
 ["AAA", "AAB", "ABA", "ABB", "BAC"]))


            
                
            


