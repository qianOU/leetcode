class Solution:
    # 解法一 ： 不太优雅
    def exclusiveTime(self, n: int, logs):
        ans = [0] * n
        mask = []
        fun = lambda x: [int(j) if j.isdigit() else j for j in logs[x].split(':')]
        for i in range(len(logs)):
            item = fun(i)

            if item[1] == 'start': # 开启任务进栈
                mask.append(item[0])
            else: # 结束任务出栈
                mask.pop()

            if i:
                top = fun(i-1)
                mode = (top[1], item[1]) # 比对最近两个任务的状态，不同的状态用不同的计算公式
                if mode == ('start', 'start'):
                    inc = item[-1] - top[-1] 
                    ans[top[0]] += inc 
 
                elif mode == ('start', 'end'):
                    inc = item[-1] - top[-1] + 1
                    ans[top[0]] += inc 

                elif mode == ('end', 'start'):
                    inc = item[-1] - top[-1] - 1
                    if len(mask) >= 2: # 由于最后 一个 元素是 start，意味着入栈，而外面要寻觅的是前一个任务，所以是 取倒数第二个 元素
                        ans[mask[-2]] += inc 
                else:
                    inc = item[-1] - top[-1]
                    ans[item[0]] += inc
        
        return ans

    
    # 解法二： 只考虑 start -- end 这一种对应关系
    # 例如，"0:start:0","1:start:5","1:end:6","0:end:9", 则 0 的 独占时间是 0-end - 0-start的时间，再减去 1 的独占时间即可
    def exclusiveTime(self, n: int, logs):
        res = [0] * n
        stack = []
        for s in logs:
            temp = s.split(':')
            if temp[1] == 'start':
                stack.append(temp)
            else: # start - end 的对应关系
                time = int(temp[2]) - int(stack.pop()[2]) + 1
                res[int(temp[0])] += time
                if stack: # 如果还有没结束的任务
                    res[int(stack[-1][0])] -= time   # 将上一个任务的独占时间减少 当前任务的独占时间
        return res
        
print(Solution().exclusiveTime(8,["0:start:0","1:start:5","2:start:6","3:start:9","4:start:11","5:start:12","6:start:14","7:start:15","1:start:24","1:end:29","7:end:34","6:end:37","5:end:39","4:end:40","3:end:45","0:start:49","0:end:54","5:start:55","5:end:59","4:start:63","4:end:66","2:start:69","2:end:70","2:start:74","6:start:78","0:start:79","0:end:80","6:end:85","1:start:89","1:end:93","2:end:96","2:end:100","1:end:102","2:start:105","2:end:109","0:end:114"]))