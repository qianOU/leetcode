# In[通过队列解决 约瑟夫环问题]
import queue

def huang(n, m):
    """
    Parameters
    ----------
    n : TYPE
        一共n位游戏者.
    m : TYPE
        喊道m的退出，其余继续游戏.

    Returns
    -------
    最后存活者的序号

    """
    q = queue.Queue()
    for i in range(1, n):
        q.put(i)
    while q.qsize() !=1:
        for i in range(m):
            s = q.get()
            if i != m-1:
                q.put(s)
    
    print(q.get())
    

huang(30, 10)

# In[ 回溯 八皇后问题]
boarder = [['.']*8 for i in range(8)] #初始化棋盘

def isvalid(boarder, row, col):
    # 处理列是否冲突
    flag = True
    #同一列
    if '+' in [boarder[i][col] for i in range(row)]: flag = False
    #右上角
    elif '+' in [boarder[i][j] for i, j in 
                    zip(range(row-1, -1,-1), range(col+1, len(boarder)))]: flag = False
    #左上角
    elif '+' in [boarder[i][j] for i, j in 
                    zip(range(row-1, -1,-1), range(col-1, -1,-1))]: flag = False
    return flag


results = []
def eight_queen(boarder, row):
    # base case
    if row >= len(boarder):
        results.append('\n\r'.join(','.join(i) for i in boarder))

    # 
    for col in range(len(boarder)):
        if not isvalid(boarder, row, col):
            continue
        
        #做选择
        boarder[row][col] = "+"
        #下一层决策
        eight_queen(boarder, row+1)
        #回退
        boarder[row][col] = '.'
        
eight_queen(boarder, 0)
print('共用%d种解法', len(results))

# In[动态规划 -- 最少找零钱问题]
nums = [5,10,50,100] #可能的货币组合方式
amounts = 123 #金钱数目



def db(nums, amounts):
    db_array = [amounts+1]*(amounts+1) # db数组
    db_array[0] = 0 # base-case
    for i in range(1, amounts+1): #自底向上的方法
        res = amounts+1 
        for coin in nums:
            if i - coin < 0: continue #跳过无解的子问题
            res = min(res, db_array[i-coin]+1) # 状态转移方程
        db_array[i] = res #更新状态i所需的最少零钱组合数
    
    return db_array[amounts] if db_array[amounts]!=amounts+1 else -1 #判断是否有解

print(db(nums, 125))


# 动态规划 自顶向下 递归调用
from functools import lru_cache

@lru_cache(100) #备忘录
def db_iter(amounts):
    if amounts == 0: # base-case
        return 0
    
    if amounts < 0: #子问题无解的情况
        return -1
    
    res = float('INF') 
    
    for coin in nums: #做选择
        temp  = db_iter(amounts-coin) #最优子问题
        if temp == -1:
            continue
        res = min(res, temp+1) #状态转移方程
    
    return res if res != float('inf') else -1
print(db_iter(125))

# In[BFS 广度优先算法]
#可以用于搜寻最短路径问题
# 借助队列实现
#以密码锁所需最少试验次数为例 初始密码为 0000

# import queue
import itertools

#将密码锁往上调整 即 9-0
def next_state(state, index, type_='up'):
    s = int(state[index])
    if type_ == 'up':
        s = s+1 if s<9 else 0
    elif type_ == 'done':
        s = s-1 if s>=1 else 9
    return state[:index] + str(s) + state[index+1:]


def bfs(start='0000', target='1214'):
    # 路径列表
    route_list = []
    q = queue.Queue() #存放每一次更新的所有可能的状态
    visited = set() #存放走过的状态，避免回路的发生
    q.put(start)
    visited.add(start)
    
    step = 0
    while(not q.empty()): #每一次的while循环相当于走了一步
       route = set()
       length = q.qsize()
       for i in range(length):
           cur = q.get(i)
           # visited 不适合放在此处是因为还未来得及取出的队列元素，
           # 很可能造成与下面更新的状态发生重复，浪费效率
           route.add(cur)
           if cur == target:
               route_list.append(route)
               return step, route_list
           # 得到当前状态下一步可能的状态
           for type_,index in itertools.product(('up','done'), range(len(cur))):
               temp = next_state(cur, index, type_)
               if temp not in visited: #如果是未经历过的状态
                   q.put(temp) #入队列
                   visited.add(cur) #记录已经走过的状态
       route_list.append(route)
       step += 1
       # route_list.append(route)
    return step if step != 0 else -1

len1, route_list1 = bfs('000', '174')
_, route_list2 = bfs('174', '000')

ans = []
for i, j in zip(route_list1, route_list2[::-1]):
    ans.append(i&j)

# 回溯算法进行打映输出
def isvalid1(s): # 返回状态s一步转移的所有情况
    temp = set()
    for type_,index in itertools.product(('up','done'), range(len(s))):
        temp.add(next_state(s, index, type_))
    return  temp

visited = set() #记录走过的状态防止回路的产生


def Print(step, path):
    if step >= len(ans): #记录回溯走到了最后一层
        return -1
    select = path[-1] #得到现在位于的状态信息
    temp = isvalid1(select) if select!='' else ans[step] 
    for s in ans[step] & temp: #将BFS得到的某一步所有可能和当前状态下步状态取交集
        if s in visited: # 如果是已经访问过的状态则跳过
            continue
        visited.add(s)
        path.append(s) # 做选择
        if Print(step+1, path) == -1: # 下一步的决策，并且只返回一条最短路径
            print('-'.join(path[1:]))
            return
        path.pop() # 回溯, 取消选择

Print(step=0, path=[''])

# 已知目标的双向bfs

def double_bfs():
    q1 = set() # 存放一个起点的集合
    q2 = set() # 存放另外一个起点的集合
    visited = set()
    step = 0
    
    q1.add('00000') # start
    q2.add('17924') # target
    while (len(q1) and len(q2)):
        # 用于交换 q1, q2的暂时队列
        temp = set()
        
        if len(q1) > len(q2):
            q1, q2 = q2, q1
        
        for cur in q1:
            if cur in q2:
                break
            for type_,index in itertools.product(('up','done'), range(len(cur))):
                one = next_state(cur, index, type_)
                if one in visited:
                    continue
                temp.add(one)
                visited.add(one)
                
        step += 1
        q1, q2 = q2, temp
    return step if step != 0 else -1

print(double_bfs())


# In[二分查找]

## 左闭右开
nums = [1,2,2,3,3,3,4,4,5,6,7,8]

#1. 普通二分查找
def binary_search(nums, target):
    left, right = 0, len(nums) #搜索区间为左闭右开的情况
    while(left < right):
        mid = int((left+right)/2)
        
        if nums[mid] == target: return mid #找到目标就返回
        elif nums[mid] > target: right = mid 
        elif nums[mid] < target: left = mid+1
    
    print(left)
    return -1


binary_search(nums, 90)

# 搜索左边界
def left_bound(nums, target):
    left, right = 0, len(nums) #左闭右开
    
    while(left < right): 
        mid = int((left+right)/2)
        
        if nums[mid] > target: right = mid
        elif nums[mid] < target: left = mid + 1
        elif nums[mid] == target: right = mid
    
    # 若找到，最后所要查询的就是mid的位置，也即是right的位置，即退出循环时left的位置
    
    # while循环的结束标志是 left == right 即left 变化范围为为 [0, len(nums)]
    print(left)
    # 为了确保数组索引不超出，所以在if中需要先判断left值是不是超过索引下标了
    return -1 if left == len(nums) or nums[left]!=target else left 

left_bound([1,2,3,4,4,4,4,5], 9)

# 右边界
def right_bound(nums, target):
    left, right = 0, len(nums) # 左闭右开
    
    while left < right:
        mid = int((left+right)/2)
        
        if nums[mid] > target: right = mid
        elif nums[mid] < target: left = mid+1
        elif nums[mid] == target: left = mid + 1
        
    # 若找到，则最后所要查询的就是mid的位置，也即是 left-1 的位置
    
    # while循环的结束标志是 left == right 即left 变化范围为为 [0, len(nums)]
    # left - 1 的变化范围是[-1, len(nums)-1]
    print(left)
    # 为了确保数组索引不超出，所以在if中需要先判断left -1 值是不是超过索引下标了
    return -1 if left == 0 or nums[left-1] != target else left -1

right_bound([1,2,3,4,4,4,4,4,5,7], 4)

##------------------- 左闭右闭
# 普通二分查找
def bin_s(nums, target):
    left, right = 0, len(nums)-1
    
    while left <= right:
        mid = int((left+right)/2)
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        
    return -1

# 搜索左边界
def left_s(nums, target):
    left, right = 0, len(nums)-1
    
    while left <= right:
        mid = int((left+right)/2)
        
        if nums[mid] == target:
            right = mid -1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        
    return -1 if left >= len(nums) or nums[left]!=target else left


# 搜索右边界
def right_s(nums, target):
    left, right = 0, len(nums)-1
    
    while left <= right:
        mid = int((left+right)/2)
        
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        
    return -1 if right < 0 or nums[right]!=target else right


# 二分搜索，还可以用于求谷底，即两个相反的单调序列的交点
def binary_search(num1, num2):
    """
    假设等长的情况, 并且num1递增，num2递减
    """
    left, right = 0, len(num1)-1
    
    while left <= right:
        mid = int((left + right)/2)
        
        if num1[mid] > num2[mid]:
            right = mid - 1
        elif num1[mid] == num2[mid]:
            return mid
        else:
            left = mid + 1
    
    return -1

print(binary_search([1,2,3,4,5,6,7,8,9], [9,8,7,6,5,4,3,2,1]))

# In[混动窗口]
from collections import defaultdict
# 最小覆盖子串

def min_sub(s, t):
    left, right = 0, 0 #搜索区间为左开右闭
    window = defaultdict(int) #保持窗口字符串信息
    need = defaultdict(int)
    for i in t:
        need[i] += 1 #初始化待匹配的子串信息

    start, length = 0, float('inf') #控制输匹配结果
    valid = 0 #控制窗口中字符串与待匹配字符串的匹配信息
    while right < len(s):
        c = s[right]
        right += 1 #移动右指针

        if  need.get(c):
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        while valid == len(need): # 滑动窗口里面含有解时，做优化
            # 记录短子串 
            if right - left < length:
                start = left
                length = right - left

            d = s[left]
            left += 1 #移动左指针

            if need.get(d):
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return s[start:start+length] if length < float('inf') else -1


print(min_sub('ADBECFEBANC', 'ABC'))


# 字符串排列

def str_premute(s, t):
    left, right = 0, 0
    need, window = defaultdict(int), defaultdict(int)
    for i in t:
        need[i] += 1
    
    valid = 0

    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        
        while right - left == len(t): #当长度匹配时，就进行移动左指针
            if valid == len(need):
                return s[left:left+len(t)]
            
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -=1
        
    return -1

print(str_premute('ADBECFEBANC', 'NBA'))

# 第二种写法，其实就是交换了 1 和 2 的逻辑顺序
def str_premute2(s, t):
    left, right = 0, 0
    need, window = defaultdict(int), defaultdict(int)
    for i in t:
        need[i] += 1
    
    valid = 0

    while right < len(s): 
        c = s[right]
        right += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        
        while valid == len(need):             # 1·先找到可行解（窗口覆盖子串），可能长度是不相等的情况
            if right - left == len(t):        # 2
                return s[left:left+len(t)]
            
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -=1
        
    return -1
print(str_premute2('ADBECFEBANC', 'NBA'))

# 最长无重复子串
def no_rep_sub(s):
    left, right = 0, 0
    window = defaultdict(int)
    
    start, length = 0, 0
    while right < len(s):
        c = s[right]
        right += 1
        window[c] += 1
        
        #因为这里while循环的条件是代表窗口里面有重复字符，题目要求最长无重复子串，
        #所以需要在while循环结束之后，再更新最长无重复子串信息
        while window[c] > 1: 
            d = s[left]
            left += 1
            window[d] -= 1
        
        # 内层循环结束，窗口内都是无重复子串，接下来只需选择最长即可
        if right - left > length: #在外面
                start = left
                length =right-left
    return s[start:start+length] if length != 0 else -1

print(no_rep_sub('bASAADFFEFFGHRTHRTJYUTIYUI8Oaabab'))
        



# In[第二章  动态规划]

# 最长递归子序列 Longest Increasing Subsequence [LIS]
def LIS(nums):
    db = [1]*len(nums) # db{i]代表 以nums[i]为结尾的最长子序列长度, base-case 全部设定为1，即为自身

    for i, j in enumerate(nums):
        for i_b, j_b in enumerate(nums[:i]):
            if j > j_b:
                db[i] = max(db[i], db[i_b]+1) #一定比某些序列最后一位小于本身的加一
    return max(db)

print(LIS([10, 9, 2,5,3,7,101,18]))

# 使用二分左侧边界方法来加速（优化算法）
def LIS_2(nums):
    # tops = [float('inf')]*len(nums) # 储存在牌堆顶部的牌
    # 注意这种算法是有数学保证的，但是牌堆得到的序列一般都不是我们想要的LIS
    tops = [0]*len(nums) #更节省内存，排队顶初始化全为 0
    
    heap  = 0 # 初始化的牌堆个数. 用heap 控制 真正的牌堆顶部数组
    for target in nums:
        left, right = 0, heap #右指针为 heap
        while left < right:
            mid = int((left+right)/2)
            
            if tops[mid] == target:
                right = mid
            elif tops[mid] < target:
                left = mid + 1
            elif tops[mid] > target:
                right = mid
        
        if left == heap: #没找到合适的牌堆，新建一个牌堆
            heap += 1
            
        tops[left] = target # 将牌放在二分左边界找出的堆顶
    # print(tops[:heap])  # 注意这种算法是有数学保证的，但是牌堆得到的序列一般都不是我们想要的LIS
    return heap #返回牌堆数 就是 LIS的长度

print(LIS_2([10, 9, 2,5,3,7,101,18]))


# 二维递增子序列 --信封嵌套问题
def message_emb(nums:int)->int:
    nums = sorted(nums, key=lambda x: (x[0],-x[1])) # 技巧：对第二维度进行倒序排放，可以确保在一维相同的情况下，LIS搜寻出来的就是只有一个
    return LIS_2([i[1] for i in nums]) # 对第二维度搜寻 LIS 最长递增子序列

print(message_emb([[1, 8],
       [2, 3],
       [5, 4],
       [5, 2],
       [6, 7],
       [6, 4]]))



# 最大子数组问题 自底向上
def maxSubArray(nums):
    dp = [nums[0]] * len(nums) #dp[i] 表示 以nums[i]为结尾的最大子数组和
    dp[0] = nums[0]
    for i, j in enumerate(nums[1:], 1):
        # 简洁的写法
        # dp[i-1] 已经代表了 前面i-1个的最大子数组和
        # 两个选择, 状态为 以nums[i]为结尾的最大子数组和
        #假设已经算出了dp[i-1],则dp[i]有两个选择,其一是与前面相邻的子数组进行连接,形成一个和更大的子数组,
        # 要么,不与前面的子数组相连接,自己作为一个子数组
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        # if nums[i] >= 0: dp[i] = dp[i-1] + j
        # dp[i] = max(dp[i], dp[i-1]) # dp[i-1] #错误的状态转移方程,状态转移方程要比较的是在不同选择下的值

    return max(dp)

print(maxSubArray([-3,1,3,-1,2,-4,2]))

# 最大子数组和问题 进行状态压缩
# 因为dp[i] 只与 dp[i-1]相关
def maxSubArray2(nums):
 
    dp_before = nums[0]
    res = dp_before
    for i, j in enumerate(nums[1:], 1):
        dp_cur = max(dp_before + nums[i], nums[i])
        dp_before = dp_cur
        if res < dp_cur:
            res = dp_cur
    return res

print(maxSubArray2([-3,1,3,-1,2,-4,2]))

# In[动态规划的二维数组遍历方式]
import pprint
nums = [[i*10 +j for j in range(9)] for i in range(6)]
pprint.pprint(nums)
m, n = len(nums), len(nums[0])
# 正向遍历
for i in range(m):
    for j in range(n):
        print(i, j , nums[i][j])
print('-'*50)
# 反向遍历
for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        print(i, j , nums[i][j])
print('-'*50)
# 斜向遍历
for k in range(n): #对长宽表都能做到斜线遍历                                   
    for i in range(n-k):
        j = k + i
        if j >= n or i >= m: #控制行索引和列索引越界
            continue
        print(i, j, nums[i][j])
        
print('-'*50)
#书上的斜线遍历 只针对 宽表, 没有处理长表超过索引的情况
for l in range(2, n+1):
    for i in range(0, n-l+1):
        j = l+i-1
        print(nums[i][j])
        
        
# In[最长公共子序列]
# 自底向上的情况
def LCS(str1, str2):
    # dp[i][j] 表示 str1[:i] 与 str2[:j] 两个字符串之间的最长公共子序列长度 [即状态的意义]
    dp = [[0]*(1+len(str2)) for i in range(1+len(str1))]
    # base case 
    for i in range(1 + len(str2)):
        dp[0][i] = 0
    for i in range(1 + len(str1)):
        dp[i][0] = 0
    
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            # 做选择
            # 其一是str1 与 str2 的新字符相等,即都落入到 LCS 中
            if str1[i-1] == str2[j-1]: 
                dp[i][j] = 1 + dp[i-1][j-1]
            else: # 其二是 str1 与 str2 的新字符不相等,也就意味着至少有一个新字符不落入到 LCS 中
            # 由于两个都未落入时,LCS的长度等于 dp[i-1][j-1] 是小于等于 dp[i-1][j]
            # 所以比较获取最大值时, 可以忽略 dp[i-1][j-1]的情况
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
    
    return dp[len(str1)][len(str2)]


print(LCS('abcdefdg', 'acebg'))

import functools
# 自顶向下的设计模式
def LCS_up(str1, str2):
    
    @functools.lru_cache(100)
    def dp(i, j): #i,j 为字符串指针位置,初始值设为字符串末尾
        # base_case
        if i == -1: return 0
        if j == -1: return 0
        
        if str1[i] == str2[j]: # 做选择的过程,可以参考上面的注释
            return dp(i-1, j-1) + 1
        
        else:
            return max(dp(i-1, j), dp(i, j-1))
    
    return dp(len(str1)-1, len(str2)-1)

print(LCS_up('abcdefdg', 'acebg'))


# In[编辑距离]
# 自顶向下
def minDistance(str1, str2):
    """
    str1:'待修改的字符串'
    str2:'希望得到的字符串'
    从字符串末尾开始进行编辑修改
    """
    @functools.lru_cache(100)
    def dp(i, j): # i 为str1的指针, j 为str2的指针

        if i == -1: return j + 1 # str1到头部,需要补j+1个字符
        if j == -1: return i + 1 # str2指针到头部,需要删除str1的i+1个字符
        
        if str1[i] == str2[j]: #字符匹配不进行修改,指针同时移动
            return dp(i-1, j-1)
        
        else: #字符不匹配,采用最少编辑次数的手段
            return min(
                dp(i-1, j) + 1, #执行删除
                dp(i, j-1) + 1, # 执行插入
                dp(i-1, j-1) +1 # 执行替换
                )

    return dp(len(str1)-1, len(str2)-1)

print(minDistance('intention', 'execution'))


# 自底向上
#dp[i][j] 表示从 str1[:i] 到 str2[:j]的最短编辑距离
def minDistance2(str1, str2):
    """
    str1:'待修改的字符串'
    str2:'希望得到的字符串'
    从字符串末尾开始进行编辑修改
    """
    dp = [[0]*(1+len(str2)) for i in range(1+len(str1))]
    # base case 
    for i in range(1 + len(str2)):
        dp[0][i] = i #代表str1为空字符时,需要增加的字符次数
    for i in range(1 + len(str1)):
        dp[i][0] = i #代表目标str2是空字符时,需要删除字符的次数
        
    for i in range(1, 1+len(str1)):
        for j in range(1, 1+len(str2)):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] #字符相同不执行更改
            else:
                dp[i][j] = min(
                    dp[i-1][j]+1, # 删除
                    dp[i][j-1]+1, # 插入
                    dp[i-1][j-1] +1 #替换 
                    )
            
    return dp[len(str1)][len(str2)]

print(minDistance2('intentione', 'executionwwe'))

# 状态压缩
def minDistance3(str1, str2):
    """
    str1:'待修改的字符串'
    str2:'希望得到的字符串'
    从字符串末尾开始进行编辑修改
    空间花销是 4+ len(str2) << len(str1) * len(str2) 构成的 dp表
    """
    # 由于发现每次更新时只和三个状态有关系,所以可以进行空间的压缩
    dp = [[0]*2 for i in range(2)]
    code =  list(range(1, 1+len(str2))) #存放换行扫描时, str2每一个位置在上一次扫描时的状态
    for i in range(1, 1+len(str1)):
        dp[0][0] = i-1
        dp[1][0] = i
        
        for j in range(1, 1+len(str2)):
            dp[0][1] = code[j-1]
            if str1[i-1] == str2[j-1]:
                dp[-1][-1] = dp[0][0] #字符相同不执行更改
            else:
                dp[-1][-1] = min(
                    dp[0][1]+1, # 删除
                    dp[1][0]+1, # 插入
                    dp[0][0] +1 #替换 
                    )
            code[j-1] =  dp[1][1]
            dp[1][0] = dp[1][1]
            dp[0][0] = dp[0][1]
        
    return dp[-1][-1]

print(minDistance3('intentione', 'executionwwe'))

# 不等权编辑距离问题
# 删除 和 替换的权重为 2， 替换的权重为1
def weighted_minDistance(str1, str2):
    """
    str1 是需要修改的字符串，
    str2 是目标字符串
    """
    dp = [[0]*(1+len(str2)) for i in range(1+len(str1))]
    # base -case
    for i in range(1+len(str1)):
        dp[i][0] = i
    for i in range(1+len(str2)):
        dp[0][i] = i
        
    for i in range(1, 1+len(str1)):
        for j in range(1, 1+len(str2)):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:# 使用不同的权值
                dp[i][j] = min(
                    dp[i-1][j] + 1/2, #删除,
                    dp[i][j-1] + 1/2, #增加
                    dp[i-1][j-1] + 1 #替换
                    )
    return dp[-1][-1]

print(weighted_minDistance('abc', 'cbad'))

# 允许相邻字符交互操作
def minDistance5(str1, str2):
    """
    str1 是需要修改的字符串，
    str2 是目标字符串
    """
    dp = [[0]*(1+len(str2)) for i in range(1+len(str1))]
    # base -case
    for i in range(1+len(str1)):
        dp[i][0] = i
    for i in range(1+len(str2)):
        dp[0][i] = i
        
    for i in range(1, 1+len(str1)):
        for j in range(1, 1+len(str2)):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else : 
                dp[i][j] = min(
                    dp[i-1][j] + 1, #删除
                    dp[i][j-1] + 1, # 增加
                    dp[i-1][j-1] + 1,#替换
                    (dp[i-2][j-2] +1) if i >1 and j > 1 else float('inf') # 根据字符数判断是否允许相邻字符交互操作
                    )

    return dp[-1][-1]

print(minDistance5('abc', 'tcbds'))

# [打映修改路径]
from collections import namedtuple

# value 存储的是最少的编辑次数
# type = 1：删除， 2：插入  3：替换
Node = namedtuple('Node', 'value type')


def minDistance2(str1, str2):
    """
    str1:'待修改的字符串'
    str2:'希望得到的字符串'
    从字符串末尾开始进行编辑修改
    """
    dp = [[0]*(1+len(str2)) for i in range(1+len(str1))] #dp数组是特殊的结点类型的集合
    # base case 
    for i in range(1 + len(str2)):
        dp[0][i] = Node(i, 2) #代表str1为空字符时,需要增加的字符次数
    for i in range(1 + len(str1)):
        dp[i][0] =  Node(i, 1) #代表目标str2是空字符时,需要删除字符的次数

    for i in range(1, 1+len(str1)):
        for j in range(1, 1+len(str2)):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = Node(dp[i-1][j-1].value, 0) #字符相同不执行更改
            else:
                temp = [
                    dp[i-1][j].value+1, # 删除
                    dp[i][j-1].value+1, # 插入
                    dp[i-1][j-1].value+1 #替换 
                    ]
                res = min(temp)
                dp[i][j] = Node(res, temp.index(res) + 1)
            
    return dp #返回dp数组，用于打映路径


# 打映 最短编辑过程， 注意只针对 等权重的插入，删除，替换操作
def display(str1, str2):
    dp = minDistance2(str1, str2)
    def route(type_):
        '''
        注意这里的打印输出要记得所有的修改例如（插入，删除，替换），
        只是在索引位置（i，j）进行更改，其它位置要保持不变
        '''
        nonlocal str1, str2, i, j, count
        count += 1
        if type_ == 1:
            
            print('%d step: delete %s from %s, before %s, after %s' 
                  %(count, str1[i-1], str1, str1,str1[:i-1]+ str1[i:]))
            str1 = str1[:i-1] + str1[i:] # 删除 str1 索引为 i-1的元素
            i -= 1
        elif type_ == 2:
            print('%d step: insert %s into %s, before %s, after %s' 
                  %(count, str2[j-1], str1, str1, str1[:i] + str2[j-1] + str1[i:]))
            str1 = str1[:i] + str2[j-1] + str1[i:] #在 str1 索引为 i-1的位置插入 str2[j-1]
            j -= 1
        elif type_ == 3:
            print('%d step: replace %s with %s, before %s, after %s' 
                  %(count, str1[i-1], str2[j-1], str1, str1[:i-1] + str2[j-1]+ str1[i:]))
            str1 = str1[:i-1] + str2[j-1] + str1[i:] #将 str1 索引为 i-1的位置替换为 str2[j-1]
            i -= 1
            j -= 1
        elif type_ == 0: #相同字符不进行操作，直接移动索引位置
            i -= 1
            j -= 1
            count -= 1

    i, j = len(dp) -1, len(dp[0]) -1
    count = 0
    while i!=0 and j!=0: #注意 dp数组里面index=0的都是base-case,代表空字符
        type_ = dp[i][j].type

        route(type_)
        
    # 删除多余的首部字符
    while (i > 0):
        count += 1
        print('%d step: delete %s from %s, before %s, after %s' 
              %(count, str1[i-1], str1, str1,str1[:i-1]+ str1[i:]))
        str1 = str1[:i-1] + str1[i:] # 删除 str1 索引为 i-1的元素
        i -= 1
    
    # 补充缺少的首部字符
    while j > 0:
        count += 1
        print('%d step: insert %s into %s, before %s, after %s' 
              %(count, str2[j-1], str1, str1, str1[:i] + str2[j-1] + str1[i:]))
        str1 = str1[:i] + str2[j-1] + str1[i:] #在 str1 索引为 i-1的位置插入 str2[j-1]
        j -= 1
    
    assert count == dp[-1][-1].value
display('intention', 'qwqweqintention')

# In[最长回文子序列]

def LongHuiSub(str1):
    n = len(str1)
    # dp[i][j] 表示的是 子字符串 str1[i,i+1,...,j] 的 最长回文子序列
    dp = [[0]*n for i in range(n)]
    # base_case 主对角线全为1， 下三角元素全为 0（因为 i>j 是不存在子串的）
    for i in range(n):
        dp[i][i] = 1 # 一个字符时， 最长回文子序列的长度为1
    
    #遍历方式一 从下往上， 从左往右
    # for i in range(n-2, -1, -1):
    #     for j in range(i+1, n):
    #         if str1[i] == str1[j]:
    #             dp[i][j] = dp[i+1][j-1] + 2
    #         else:
    #             dp[i][j] = max(
    #                 dp[i][j-1],
    #                 dp[i+1][j]
    #                 )
                
    # 遍历方式二: 斜向遍历
    for k in range(1, n):
        for j in range(k, n): #后遍历列，注意从k开始
            i =  j - k #优先行更新
            if str1[i] == str1[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

print(LongHuiSub('aecda'))


# 最长回文子序列 进行状态压缩
def LongHuiSub2(str1):
    n = len(str1)
    dp = [1] * n # 为优化前的dp二维数组的竖向投影值
    
    for i in range(n-2, -1, -1):
        pre = 0 #dp[i+1][j-1] 根据base-case 可以知道值为 0
        for j in range(i+1, n):
            temp = dp[j] # dp[i+1][j]
            if str1[i] == str1[j]:
                dp[j] = pre + 2
            else: 
                dp[j] = max(temp, dp[j-1]) # dp[j-1] = dp[i][j-1]
            pre = temp # 行右向扫描移动，更新dp[i+1][j-1]
    return dp[n-1]

print(LongHuiSub2('aecda'))


1# In[最小插入次数构建回文串]

def MinHuiSub(str1):
    n = len(str1)
    # dp[i][j] 表示的是 子字符串 str1[i,i+1,...,j] 的 最小插入次数才能构建成回文串
    # base -case 下三角全为0， 主对角线也全为0（因为一个字符本身就是回文串）
    dp = [[0]*n for i in range(n)]
    
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if str1[i] == str1[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(
                    dp[i+1][j] + 1, # 子串的右侧进行插入
                    dp[i][j-1] + 1  # 子串的左侧进行插入
                    )
                # dp[i][j] = min(dp[i+1][j], dp[i][j-1])+1
    return dp[0][n-1]

print(MinHuiSub('abceadf'))


# In[正则表达式]

from functools import lru_cache

# 对于需要穷举的程序，都可以利用动态规划解决
# 如果对象是字符串，状态的构造一般基于字符串指针
def regExp(str1, str2):
    """
    str1: 为待匹配的字符串
    str2: 为正则表达式，只支持 . 和 *
    """
    #从两个字符串头部开始扫描，此题不适合用dp数组，因为正则表达式采用了通配符
    
    @lru_cache(1000) #备忘录，解决计算重复子问题
    def dp(i, j): #i, j 分别为 str1， str2的指针 # 状态 即为双指针
        # base case
        # 情形1：
        if j == len(str2): # 正则字符串走到尾部
            return i == len(str1) # 只有字符串指针也走到末尾才返回 真
        if i == len(str1): #字符串走到末尾
        #只有当剩下的正则表达式每个字符后面都跟着通配符 * 表示0匹配时。才返回匹配成功
            if (len(str2)-j)%2: return False
            elif all(str2[i]=='*' for i in range(j+1, len(str2),2)): return True
            return False
        
        
        # 此题动态规划的选择 主要体现在：str2[j]匹配几个str1的字符上
        if str1[i] == str2[j] or str2[j] == '.': #如果当前字符匹配
            if j < len(str2) - 1 and str2[j+1] == '*': #判断下一个通配符是不是 *
            ##情况一：eg: [aaaa, a*] 表示匹配 任意多个str1[i], 这里左的就是固定str2的指针，让str1的指针继续向前移动一位
            # 情况二: eg：[aa, a*aa] 这就表明 * 只能匹配 0 项，即固定str1指针，str2指针又移动2位
                return dp(i+1, j) or dp(i, j+2)#采用 or 实现两种情况的遍历
            else:
                return dp(i+1, j+1) #如果不是 *，两个指针都需要向前移位
        
        elif str1[i] != str2[j] and str2[j] != '.': # 判断当前字符不匹配
            if j < len(str2) - 1 and str2[j+1] == '*': # 判断下一个通配符是不是 *
                return dp(i, j+2) # 匹配0项。 由于当前字符不匹配，但是下一位是通配符 *，也就是str2指针移动两位
            else:
                return False
    
    return dp(0, 0) # 从 0，0 开始扫描

print(regExp('zaaab', '.a*b'))
print(regExp('anrbd', 'a..b'))
print(regExp('anrb', 'a*anrb'))


# In[四键盘问题]

from functools import lru_cache
# 全暴力搜寻最佳解
# 由于 pri, mem 都是不定数。所以需要使用自顶向下的递归方式
@lru_cache(100) # 解决重复子问题
def cal_one(N):
    def dp(n, pri, mem):
        """
        n: 操作次数
        pri: 第n次操作。屏幕上显示的字符数量
        mem: 粘贴板中的字符数量
        """
        # base case
        if n >= N:
            return pri

        # 做选择
        return max(
            dp(n+1, pri+1, mem), # 按 A键
            dp(n+1, pri+mem, mem), #按 ctrl - v 键
            dp(n+2, pri, pri) # 按 ctrl A 和 ctrl + C 即全选+复制,所以相当于走了两个步骤
            )
    return dp(0, 0, 0)

print(cal_one(7))
# 复杂度太高了！！！！

# 提出 四键盘问题的优化算法
# 主要手段，通过人为分析，通过降低状态空间的维数来去除不必要的枚举
"""
简答描述一下，人为分析得到的最佳方案，有如下两种：
1. 一直打映输出 A （对于N较小的时候，是最佳的）
2. A,A,A,ctrl-A,ctrl-c, ctr-v, ctr-v, ctrl-A,ctrl-c, ctr-v (对于N比较大时是最优的)
换句话说就是最后一次要不是 A， 要不就是 ctrl + v
"""
def optFourKeyboard(N):
    dp = [0] * (N+1) # dp数组含义：dp[i] 表示 共经过i次操作能打映输出的最多字符数
    # base case
    dp[0] = 0 #即不进行操作的时候，字符数为 0
    
    for i in range(1, N+1):
        dp[i] = dp[i-1] + 1 #按  A键 的情况
        # 做选择，选择的表示用上一次按ctrl-A + ctrl + C的时机来表示
        for j in range(2, i): # j 表示上一次按 ctrl-A + ctrl + C 的时机，遍历所有的可能
        # dp[j-2]表示粘贴板中的字符数，i-j表示连休复制粘贴的次数，+1 则是因为原本的屏幕数据也要汇总
            dp[i] = max(dp[i], dp[j-2] * (i-j+1)) # 按 ctrl + v 的情况
    return dp[N]

print(optFourKeyboard(7))




# In[高楼扔鸡蛋问题]

from functools import lru_cache

# 寻常思路
# 复杂度为 : (K*N)*N
def popEgg(k, n):
    """
    k: 表示鸡蛋数目
    n： 表示楼的层数
    返回 m：在k个鸡蛋的限制下，在最坏的情况时，
    利用最少的测量次数m表示抛鸡蛋安全的极限楼层
    """
    @lru_cache(1000)
    def dp(i, j):
        """
        i 是限制的鸡蛋数
        j 是高楼的层数
        （i，j）组合形成 动态规划的状态
        """
        # base case
        if i == 1: return j #只有一个鸡蛋，所以只能线性搜索
        if j == 0: return 0 # 没有楼层时，表明实验次数为 0
        
        res = n
        # 做选择
        for layer in range(1, j+1): #楼层选择是 1 to j
            res =  min(
                res,
                max( #最坏情况指的就是说鸡蛋碎或者不碎两种情况中，更费次数的那种，所以取max
                    dp(i, j - layer), #鸡蛋未碎，# 向j楼以上进行搜索
                    dp(i-1, layer-1) #鸡蛋碎了，向下层楼进行搜索
                    ) + 1 #在j楼做了一次测试，需要加1
                )

        return res
    return dp(k, n)

print(popEgg(3, 14))


# 利用二分法降级子查询的复杂度
# 复杂度为（K*N）*log(N)
"""
基于下面的事实：
1. 固定 鸡蛋数量i，则随着楼层j的变大，需要的测量次数也是单调递增的(实质上不是严格单调)
    即dp(i, j)在i固定的时候随着j变大而变大
    dp(i, N-j) 在 i 与楼层总数固定的时候，随着j变大，而变小
    所以寻找     res =  min(
                res,
                # 以下形成一个 V 形状， 谷底为 单调序列的交点
                max( 
                    dp(i, j - layer), #递增
                    dp(i-1, layer-1)  #递减
                    ) + 1 
                ) 也就是寻找V行曲线的谷底
    可以利用二分搜索来优化查询
"""
def opt_popEgg(k, n):
    @lru_cache(100)
    def dp(i, j):
        if i == 1: return j
        if j == 0: return 0
        
        res = n
        
        left, right = 1, j #搜索区间为闭区间
        while left <= right:
            mid = int((left + right)/2) #在 mid 处进行试验
            not_broken = dp(i, j - mid)
            broken = dp(i-1, mid -1)
            if not_broken > broken:
                left = mid + 1
                # 此处 not_broken  为最坏的情况
                res = min(res, not_broken + 1) #每测验一次，更新一下目标值
            elif broken >= not_broken:
                # 此处 broken 为 最坏的情况
                right = mid - 1
                res = min(res, broken + 1)
            
        return res


    
    return dp(k, n)

print(opt_popEgg(8, 21))

# 重新定义状态
# 复杂度为： K*N
# 进行了问题的反向转换，十分巧妙
def opt_popEgg2(k, n):
    # dp[i][j] 表示 在 i个鸡蛋下，最多测试j次时，在最坏的情况下，最多能测量 dp[i][k]层
    dp = [[0]*(1+n) for i in range(1+k)]
    m = 0
    
    #遍历的更新方式为从左到右，从上到下
    while dp[k][m] < n:  # 退出条件为 dp[K][m] = n
        m += 1 #控制列
        for i in range(1, k+1): #更新m列的所有数据
            # dp[i-1][m-1] 表示的是在第一次测定的楼层时鸡蛋破碎，在该楼层下利用 i-1个鸡蛋，测量m-1次时，最坏情况下能测量到的楼下层数
            # 同理 dp[i][m-1] 表示是 鸡蛋未碎时，利用i个鸡蛋，最多测量m-1次时，在最坏情况下测量出的层数
            # 1则表示的是第一次测试的楼层
            dp[i][m] = dp[i-1][m-1] + dp[i][m-1] + 1
    return m

print(opt_popEgg2(8, 21))


# In[戳气球问题]

# 基于回溯算法的暴力方式
def blob(nums):
    nums = list([1, *nums, 1])
    results = [] # 记录所有的解
    
    def bp(nums, score):
        if len(nums) == 2:
            assert all([i==1 for i in nums])
            results.append(score)
            return score
        
        for i in range(1, len(nums)-1):
            # 做选择部分
            cur = nums[i]
            temp = nums[i]*nums[i-1]*nums[i+1]
            score += temp 
            nums  = nums[:i] + nums[i+1:] # 更新选项列表
            
            bp(nums, score) #回溯，下一级的决策
            
            # 恢复部分
            score -= temp # 将分数恢复
            nums.insert(i,cur) # 将气球还原到先前位置
    
    bp(nums, 0)
    return max(results) #得到最优的解

print(blob([3,1,5,8]))

# 戳气球问题的动态优化解法

# 优化的选择是用最后戳破的气球位置来表示
# 在四键盘问题中，也有类时的选择表示方式（即上一次（最后一次）全选复制的时机）

def opt_blob(nums):
    nums = list([1, *nums, 1])
    n = len(nums)
    
    # dp 数组的状态 用 开区间(i,j) 表示，即戳破（i，j）范围内的所有气球时能获得的最高分
    # 如此定义 dp数组 可以解决子问题的相关性，才能使用动态规划的方法
    dp = [[0] * len(nums) for i in range(len(nums))] # 蕴含了base-case
    # base -case
    # 由于是开区间，所以要求 j > i+1，以及 0<= i <= n-1
    
    # 遍历方式一：从下往上，从左往右
    # for i in range(n-3, -1, -1):
    #     for j in range(i+2, n):
    #         for k in range(i+1, j): #对于最后一次戳破气球的位置做选择
    #         #第一步戳破(i,k)的所有气球， 第二步戳破（k，j）的所有气球
    #         # 最后戳破 第 k 个气球
    #         # 经过巧妙的设计选择，避开了相关性的要求
    #             dp[i][j] = max(dp[i][j],
    #                            dp[i][k] + dp[k][j]+nums[i]*nums[k]*nums[j] 
    #                            )
                
    # 遍历方式二： 斜线遍历
    for k in range(2, n): #控制斜线
        for j in range(k, n): #从左往右扫描,注意起始是从斜线与第一行的交点，即k出发
            i = j - k
            for s in range(i+1, j):
                dp[i][j] = max(dp[i][j],
                               dp[i][s] + dp[s][j] + nums[i]*nums[s]*nums[j])

    return dp[0][n-1]


print(opt_blob([3,1,5,8]))

# In[0-1 背包问题]
def package(wt, vt, comp):
    """
    wt: 物品的重量数组
    vt： 物品的价值数组
    comp: 背包的容量
    """
    
    def dp(i, comp):
        """
        i: 表示选择物品的对象为前i种，
        comp : 是指背包容量
        """
        # base-case
        if i == 0:
            return 0
        if comp == 0:
            return 0
        
        res = dp(i-1, comp) #对于第i件物品，不进行选取
        if comp - wt[i-1] >= 0: # 如果第i件物品重量还在包的容量范围之内，进行选择
            res = max(res, 
                      vt[i-1] + dp(i-1, comp-wt[i-1]) #获取第i件物品
                      ) # 做选择
        return res
    
    return dp(len(wt), comp)

print(package([2,1,3], [4,2,3], 4))

# In[子集背包问题]
def canPartition(nums):
    sum_= sum(nums)
    if sum_%2: return False #如果和为奇数，也就是不能被分为和相等的两部分
    w = int(sum_/2) #得到一个背包的重量
    
    def dp(i, w):
        if w==0: return True # 如果背包容量为空，则有唯一一种装物品的方式即 为空
        if i==0: return False # 没用物品可以装满背包时，返回false
        #做选择 对于每一件物品只有两种选择，即 入袋 或则 不入袋
        res = dp(i-1, w) #不装取物品 i
        if w - nums[i-1] >= 0: #判断背包容量是否够装取物品 i
            res = res or dp(i-1, w-nums[i-1])
        return res
    return dp(len(nums), w)

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))


# 状态压缩
def canPartition2(nums):
    sum_= sum(nums)
    if sum_%2: return False #如果和为奇数，也就是不能被分为和相等的两部分
    w = int(sum_/2) #得到一个背包的重量
    n = len(nums)
    dp = [True] * (w+1) # dp数组 以及 base-case dp[0] = 0
    
    for i in range(1, n+1):
        for j in range(w, 0, -1): # 注意此处必须是倒序遍历更新dp数组
            if j - nums[i-1] >=0:
                dp[j] = dp[j] or dp[j-nums[i-1]]
    return dp[-1]

print(canPartition2([1,5,11,5]))
print(canPartition2([1,2,3,5]))


# In[完全背包问题]
def change(nums, amount):
    
    n = len(nums) # 一共几种不同面额的纸币
    # dp[i][j] 表示 使用 前 i 种面额的金钱，凑成金额 j 的组合数
    dp = [[0]*(1+amount) for i in range(1+n)]
    
    # base -case
    for i in range(1+n):
        dp[i][0] = 1 #即金额为0时，只有一种组合方式 即 空
    
    for i in range(1, amount+1):
        dp[0][i] = 0 #没有纸币时，凑不成相应的金额
    
    
    for i in range(1, n+1):
        for j in range(1, amount+1):
            # 做选择
            dp[i][j] = dp[i-1][j] # 不使用面额为 nums[i] 的货币
            if j - nums[i-1] >=0:
                # dp[i][j-nums[i-1]] 代表在使用前i种货币凑成 j 金额时，使用了面额为 nums[i] 的货币金额
                # dp[i-1][j] 代表在使用前i种货币凑成 j 金额时，没使用面额为 nums[i] 的货币金额
                # 由于dp[i][j] 表示利用前i种货币凑成j金额时总的组合数，所以是上述两种情况的和
                dp[i][j] = dp[i][j-nums[i-1]] + dp[i-1][j]

    return dp[n][amount]

print(change([1,2,5], 5))
    
# 状态压缩
def change2(nums, amount):
    n = len(nums) # 一共几种不同面额的纸币
    
    dp = [0]*(1+amount) 
    # base-case 
    dp[0] = 1
    
    for i in range(1, n+1):
        for j in range(1, amount+1):
            if j - nums[i-1] >= 0:
                dp[j] += dp[j-nums[i-1]]
    
    return dp[-1]

print(change2([1,2,5], 5))

# In[题目千变，套路不变]

# 不能相邻取钱问题--线性排列情况
def rob(nums):
    if len(nums) == 0:return -1

    dp = [0]*(len(nums)+2) # dp[i] 表示从第i家开始收钱，能获得的最多金额
    # base-case
    # dp[-1] = dp[-2] = 0
    for i in range(len(nums)-1, -1, -1):
        # 做选择
        dp[i] = max(
            dp[i+1], # 不取钱，到下一位置进行决策
            dp[i+2]+nums[i-1] # i处取钱，到 i+2 位置进行决策
            )
    
    return dp[0]

print(rob([2,1,7,9,3,1]))
# 状态压缩
# 不能相邻取钱问题--线性排列情况
def rob2(nums):
    if len(nums) == 0:return -1

    dp_1, dp_2 = 0, 0

    for i in range(len(nums)-1, -1, -1):
        # 做选择
        temp = max(
            dp_1, # 不取钱，到下一位置进行决策
            dp_2 + nums[i-1] # i处取钱，到 i+2 位置进行决策
            )
        
        dp_2 = dp_1
        dp_1 = temp
    
    return dp_1

print(rob2([2,1,7,9,3,1]))

# 不能相邻取钱问题--环形排列情况
"""
环状即意味着首位相连，首尾不能同时取到！
所以只有下面三种情况：
1. 在首部和中间部分的序列能取得金额最大值
2. 在中部和尾部分的序列能取得金额最大值
3. 只有中部序列能取得金额最大值（实际上可以不用比较这种情况，因为序列是1和2的子序列）
"""
def rob_cycle(nums):
    n = len(nums)
    if n == 1: return nums[0]
    elif not n: return -1
    # 做选择
    return max(
        rob2(nums[0:n-1]), #对应于情况 1
        rob2(nums[1:n]) #对应于情况 2
        )


# 不能相邻取钱问题--二叉树情况
def rob_binary_tree(root):
    if root is None: #叶子节点子代返回0
        return 0
    
    # 取
    sec_left = 0 if root.left is None else rob_binary_tree(root.left.left)+rob_binary_tree(root.left.right)
    sec_right = 0 if root.right is None else rob_binary_tree(root.right.left)+rob_binary_tree(root.right.right)
    get = sec_left + sec_right + root.value
    
    # 不取
    no_get = rob_binary_tree(root.left) + rob_binary_tree(root.right)
    
    # 对应两个选择进行择优
    return max(get, no_get)
    

# In[动态规划与回溯算法的关系]
# 给数组元素添加符号使得记和为目标值
# 回溯
def findTargetSumWay(nums, target):
    count  = 0
    def backtrace(index, residue):
        nonlocal count
        # base case
        if index == len(nums):
            if residue == 0:
                count += 1
            return count
        # 做选择
        for i in [1, -1]:
            residue -= i* nums[index]
            backtrace(index+1, residue) # 回溯
            # 恢复选择
            residue += i*nums[index]
    
    backtrace(0, target)
    return count

print(findTargetSumWay([1,3,1,4,2], 5))

# 动态规划解法

# 实质是子背包问题 容量为 (sum(nums) + target )/2
"""
# 注意数组全是正数的集合

 记 Sum(A) 为 分配 + 的数组子集合
 记 Sum(B) 为 分配 - 的数组子集合
 则有 Sum(A) - Sum(B) = target
 且有 Sum(A) + Sum(B) = Sum(nums)
 则有数组子集 容量为 (sum(nums) + target )/2 即子背包问题
"""
def findTargetSumWay2(nums, target):
    sum_ = sum(nums)
    if sum_<target or (sum_ + target)%2:
        return -1 #没有符合题意的解法
    cap = int((sum_ + target)/2)
    
    # dp[i][j]表示用前i件物品，在容量为j的情况下，可否通过添加符号达到目标值的总次数
    dp = [[0]*(1+cap) for i in range(len(nums)+1)]
    
    # base-case
    for i in range(len(dp)):
        dp[i][0] = 1
    
    for i in range(1, len(nums)+1):
        for j in range(1, cap+1):
            # 选择1 不取 物品 i
            dp[i][j] = dp[i-1][j]
            if 0<= j - nums[i-1]: 
                # 选择2: 取物品 i
                dp[i][j] += dp[i-1][j-nums[i-1]] #注意是总的次数,所以是两种选择情况的和
     

    return dp[len(nums)][cap]

print(findTargetSumWay2([1,3,1,4,2], 5))

# In[LRU算法]
# LRU == Least Recent Use
"""
实质是:
    哈希链表 = 哈希表 + 双向链表(保证了删除的高效性)
"""

# In[LFU算法]
#LFU = least Frequent Use
"""
实质是:
    哈希表 + 哈希链表
"""
# In[二叉搜索树操作集锦]

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

"""
BST : binary search tree
定义: 一个二叉树中,任意节点的值要大于等于左子树所有节点的值,
    且要小于等于右子树的所有节点的值
"""
# 判断BST合法性

def isValidBST(root):
    
    # 采用前序遍历法
    # 给子树所有节点添加一个范围[min, max]
    def IsValidBST(root, min_, max_):
        # 其一:根节点的操作
        if root is None:
            return True
        elif min_ is not None and root.vall < min_: return False
        elif max_ is not None and root.val > max_: return True
        
        # 交给递归处理子树的情况
        return IsValidBST(root.left, min_, root) and \
                IsValidBST(root.right, root, max_)
    
    
    return IsValidBST(root, None,None)


# 在BST中找一个数是否存在
def isInBST(root, target):
    
    # 前序遍历
    def tranvesal(root, target):
        # 根节点操作
        if root is None:
            return False
        elif root.val == target:
            return True
        
        # 遍历子树
        return tranvesal(root.left, target) or \
                tranvesal(root.right, target)
    
    return tranvesal(root, target)


# 在BST中插入一个数
def insertIntoBST(root, target):
    
    # 实质还是前序遍历
    def insert(root, target):
        # 根节点操作
        # 找到空位置插入新节点
        if root is None: return Node(target)
        # 如果已经存在,则不要重复插入,直接返回
        if root.val == target: return root
        
        # 递归部分
        # 插入右子树
        if root.val < target: 
            root.right = insert(root.right, target)
        # 插入左子树
        else:
            root.left = insert(root.left, target)
        # 递归调用的逐级返回
        return root # 注意不要忘记了!!!!
    insert(root, target)


# 在 BST 中删除一个数
def solution(root, target):
    
    # 获取在左右子树都存在的情况下的
    # 获取左子树最大值
    def getMax(root):
        while root is not None:
            prev = root
            root = root.right
        return prev
    
    # 获取右子树最小的那个值
    def getMin(root):
        while root is not None:
            prev = root
            root = root.left
        return prev
        
    # 删除节点
    def deleteBST(root, target):
        
        if root is None:
            return None
        
        # 分三种情况
        if root.val == target:
            # 情况一
            # 只有右子节点时,用右子节点进行替代 root
            if root.left is None: return root.right
            # 只有左子节点时,用左子节点进行替代 root
            elif root.right is None: return root.left
            # 情况二: 以上包含了既无左子节点也无右子节点的情况,此时返回 None,表示直接删除 root
            
            # 情况三: 左子树和右子数都存在的情况下,有两种方式,任选其一即可:
                # 1. 用左子树最大值来替代 (即 左子树的右子树伸展)
                # 2. 用右子树最小值来替代 (即 右子树的左子树延伸)
            elif root.left is not None and root.right is not None:
                change_node = getMax(root.left) # 方式 1
                change_node = getMin(root.right) #方式 2
                root.val = change_node.val # root.val 的值用找到的最优值来进行替代,不高效的操作
                root.right = deleteBST(root.right, change_node) # 对于情况2, 删除已使用替换的节点,暗中表示节点结构的改变
                return root
            
        # 递归部分
        # 去左子树寻找,进行删除
        if root.val > target:
            root.left = deleteBST(root.left, target)
        elif root.val < target:
            # 右子树结构被更改,所以左边需要右子数指针来接收新的右子树
            root.right = deleteBST(root.right, target)
        
        return root
    # 主接口,进行调用调用
    return deleteBST(root, target)

# In[完全二叉树的节点数为何那么难算]
"""
满二叉树: 每一层都是满的二叉树
完全二叉树: 每一层都是紧凑靠左排列的,(层优先,层满了才能展开下一层,顺序是从左至右)
"""

# 普通二叉树计算点的个数
# 复杂度 O(2**N)
def countNodeComm(root):
    # base-case 递归的基本出口
    if root is None:
        return 0
    # 后续遍历 : 根据 1 的位置确定遍历的方式
    return countNodeComm(root.left) + countNodeComm(root.right) + 1 # 加 1 表示当前节点的计数

# 满 二叉树
# 可以通过获得树的深度,之后利用公式计算即可
# 复杂度 O(log(N))
def countNodeFull(root):
    depth = 0

    while root is not None:
        depth += 1
        root = root.left
        
    return 2**depth - 1

# 完全二叉树
# 复杂度 O(logN * log(N))
"""
完全二叉树有个特性,那就是左子树或右子树中必然有其一是满二叉树
"""
def countNodeComp(root):
    
    if root is None:
        return 0
    
    ld = rd = 0
    right = left = root
    # 每一次调用相当于 深度遍历 即需要 logN 词
    while left is not None:
        left = root.left
        ld += 1

    while right is not None:
        right = right.right
        rd += 1
    
    # 如果 左右子树高度一致,说明是一棵满二叉树
    if ld == rd:
        return 2**ld - 1
    else:
    # 如果 左右子树高度不一致,就按照普通二叉树的逻辑计算结点树
    # 因为 root.left 或者 root.right 子树中必会有一个是满二叉树，所以实际上只有一支需要遍历（log(N)）个节点
        return 1 + countNodeComp(root.left) + countNodeComp(root.right)

# 所以总的复杂度为 (logN*logN)


# In[用各种遍历框架序列化和反序列化二叉树]
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

A = Node(1)
B = Node(2)
C= Node(3)
D = Node(4)

A.left = B
A.right = C
B.right = D

NULL = "#"
SEP = ','
# 前序遍历的解法
# 一般用可变数据类型来记录遍历的路径
def forward_serialize(root, st=[]):
    # base_case
    # 递归出口
    if root is None:
        st.append(NULL)
        return None
    
    # 前序的根节点操作
    st.append(str(root.val))
    
    forward_serialize(root.left, st)
    forward_serialize(root.right, st)

    return SEP.join(st)

print('前序遍历')
string = forward_serialize(A, [])
print(string)

# 反序列化
# 套路是 先找寻 根节点 root，之后对于子树的处理交给递归
def f_deserialize(strings):
    
    records = strings.split(SEP)
    
    def forward_deserialize(records):
        # base-case 
        if len(records)==0:
            return None
        
        # 前序根节点操作
        temp = records.pop(0) #第一个元素为根节点
        if temp == NULL:
            return None
        
        root = Node(int(temp))

        root.left = forward_deserialize(records)
        root.right = forward_deserialize(records)
        
        return root
    
    return forward_deserialize(records)


print(forward_serialize(f_deserialize(string), []))


# 后序遍历法 --序列化
def b_serialize(root, st):
    # base-case
    if root is None:
        st.append(NULL)
        return 
    
    b_serialize(root.left, st)
    b_serialize(root.right, st)
    
    # 后序操作根节点
    st.append(str(root.val))
    
    return SEP.join(st)

print('后序遍历')
string = b_serialize(A, [])
print(string)

# 后序遍历 --反序列化
def b_deserialize(strings):
    records = strings.split(SEP)
    
    def back_deserialize(records):
        # base-case
        if len(records) == 0:
            return None
        
        # 找寻根节点
        temp = records.pop()
        if temp == "#":
            return None
        root = Node(int(temp))
        
        # 先恢复右子树
        root.right = back_deserialize(records)
        root.left = back_deserialize(records)
        
        return root
    
    return back_deserialize(records)


print(b_serialize(b_deserialize(string), []))

# 中序遍历 --只能做序列化
def mid_seriallize(root, st):
    # base-case
    if root is None:
        st.append(NULL)
        return 
    
    mid_seriallize(root.left, st)
    # 中序 操作节点
    st.append(str(root.val))
    
    mid_seriallize(root.right, st)
    
    return SEP.join(st)

print('中序遍历')
print(mid_seriallize(A, []))


print('层次遍历')
import queue
# 层次遍历 
# 不需要借助 于 递归
# 主要需要借助于 队列 来实现
def layer_serializer(root):
    if root is None: return
    q = queue.Queue() # 队列用于存放，每一层的节点
    q.put(root) # 根节点入队列
    st = [] # 存放遍历路径
    while not q.empty():
        cur = q.get()
        
        if cur is None:
            st.append(NULL)
        else:
            st.append(str(cur.val))
            q.put(cur.left)
            q.put(cur.right)
            
    return SEP.join(st)

strings = layer_serializer(A)
print(strings)

# 层次遍历 反序列化
def layer_deserializer(strings):
    # tips: 为了防止使用pop 可以将records倒序存放，不过此时要先处理右节点其次才是左节点
    records = strings.split(SEP)
    if len(records) == 0:
        return 
    temp = records.pop(0)
    if temp == "#":
        return None
    q = queue.Queue() # 专门存放父节点
    root = Node(int(temp))
    q.put(root)
    
    while not q.empty():
        parent = q.get()
        left = records.pop(0)
        right = records.pop(0)
        if left != '#':
            parent.left = Node(int(left))
            q.put(parent.left)
        if right !='#':
            parent.right = Node(int(right))
            q.put(parent.right)
        
    return root

print(layer_serializer(layer_deserializer(strings)))


# In[ Git 原理之二叉树最近公共祖先]

flag = 0

# LCA = Lowest Common Ancestor
# 应用前提是每个节点都是具有唯一值
def lowestCommonAncestor(root, p, q):
    """
    root是根节点
    p是节点1的值，q是节点2的值
    目标是找寻p和q的LCA
    有以下三种情况：
        1. p和q都不存在于 以root为根节点的子树中，此时返回 None
        2. p和q只有一个节点存在于 root子树中时，此时返回其中存在的节点
        3. p和q都存在于root子树中时，返回 LCA
    """
    # base - case
    if root is None:
        return None
    if root.val in [p, q]:
        return root
    
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    
    # 后序遍历
    # 根节点操作

    # 情况 1
    if left is None and right is None:
        return None
    
    # 情况 3
    if left is not None and right is not None:
        # raise ValueError(root) 当面临存在多个相同节点的时候，可以使用抛出异常来更改递归流程，导出后续遍历的（第一个） LCA
        return root
    
    # 情况 2 ：因为二叉树中节点的值各不相同，因此如果左子树查到了LCA，则右子树查询结果必然是None
    return left if left is not None else right

print(lowestCommonAncestor(A, 4, 3).val)

# 对于二叉树中存在多个相同节点时的LCA解法
# D.left =Node(3)
# B.left = Node(5)

# try:
#     lowestCommonAncestor(A, 5, 3).val
# except ValueError as e:
#     print(e.args[0].val)
# # 

# In[特殊数据结构：单调栈]
"""
单调栈：指的是每次新元素入栈后，栈内的元素都保持单调（递增或者递减）
主要用来处理 Next Greater Element 问题
"""
# 时间复杂度 为 O(n)
# 因为每个成员入栈一次，且之多出栈一次
def nextGreaterEleMent(nums):
    # 构建一个单调栈
    stack = []
    # 构建一个容纳答案的数组
    ans = [-1]*len(nums)
    
    # 倒序入栈，也就是正序出栈
    for i, val in enumerate(nums[::-1]):
        index = len(nums) - i -1
        # 保持栈内的元素是单调递增的(栈底->栈顶)
        while len(stack) and stack[-1] <= val:
            stack.pop()
        
        ans[index] = stack[-1] if len(stack) else -1
        
        # 成员入栈.接受下一轮的保单调操作
        stack.append(val)
    
    return ans

print(nextGreaterEleMent([2,1,2,4,3]))

# 题目变形，求离next greatrer element 的相隔天数
def daliyTemprature(nums):
    # 构造一个单调栈, 确保stack里面的索引，对应的nums中的原数据是递减的
    stack = []
    
    ans = [0] * len(nums)
    
    for i in range(len(nums)-1, -1, -1):
        # 确保stack里面索引对应的数据是递减的
        while len(stack) and nums[stack[-1]] <= nums[i]:
            stack.pop()
        
        ans[i] = stack[-1] -i if len(stack) else 0 
        # 索引入栈
        stack.append(i)
    return ans

print(daliyTemprature([73, 74, 75, 71, 69, 72, 76, 73]))

# 处理 环形数组的 next greater number 情况
# 这种一般是将数组展平，并构造出双倍长的数组，其后将双倍长数组按普通数组进行处理，即可
# 巧妙：实际上，可以不用扩充数组，通过操作索引的移动就可以了
def cycle_nextGreaterElement(nums):
    
    n = len(nums)
    # 构造单调栈
    stack = []
    # 答案
    ans = [0] * len(nums)
    
    for i in range(2*n-1, -1, -1):
        while len(stack) and stack[-1] <= nums[i%n]:
            stack.pop()
        
        ans[i%n] = stack[-1] if len(stack) else -1
        
        # 数组元素入栈
        stack.append(nums[i%n])

    return ans

print(cycle_nextGreaterElement([2,1,2,4,3]))


# In[特殊数据结构： 单调队列]
"""
单调队列：就是一个队列，通过使用巧妙的方法，使得队列中的元素全部都是单调递增（或递减）的
作用： 主要用来处理滑动窗口的一系列问题，比如滑动窗口的最大值
在O(1) 的复杂度下，算出每个窗口的最大值
"""

class MonotonicQueue:
    def __init__(self):
        self.queue = list() # 模拟队列

    def push(self, val):
        # 将队列保持 单调递减 的顺序
        while len(self.queue) and self.queue[-1] <= val:
            self.queue.pop()

        self.queue.append(val)
    
    # 最大值在队列的头
    def max(self):
        return self.queue[0]
    
    # 如果遇见的是被压缩处理的状态，则不进行出队列
    def pop(self, val):
        if self.queue[0] == val:
            self.queue.pop(0)
    
    def __repr__(self):
        return ','.join(str(i) for i in self.queue)

def maxSlidingWindow(nums, k):
    # 单调递减队列
    window = MonotonicQueue() # 将窗口设定为单调队列
    ans = []
    
    for i in range(1, len(nums)+1):
        
        # 先把窗口的前 k-1 个入队列
        if i < k:
            window.push(nums[i-1])
        else: # 窗口开始向前滑动
            # 加入新值
            window.push(nums[i-1])
            # 将窗口的最大值计入结果
            ans.append(window.max())
            # 移除窗口的最左端元素
            window.pop(nums[i-k]) # i-k 为窗口最左端的索引
        # print(window)
        
    return ans

print(maxSlidingWindow([1, 3,-1,-3,5,3,6,7], k=3))

# In[判断回文链表]
# 链表的节点
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return str(self.val)

# 测试用例
head = A = Node(0)
for i in [1,2,3,4,5,6,5,4,3,2,1,0]:
    A.next = Node(i)
    A = A.next
    
# 倒序遍历链表
def traverse(head):
    if head is None:
        return 
    
    traverse(head.next)
    # 后序遍历代码，此处只是做打印输出
    print(head.val)

traverse(head)

# 使用递归 来倒序比较单链表是否是回文序列
# 时间复杂度为 O（N），
# 空间复杂度为 O（N）利用递归栈来保存结果
def isPallindrome(head):
    forward = head
    
    # 倒序遍历代码
    def traverse(head):
        nonlocal forward # 自由变量
        
        if head is None:
            return True
        
        # 需要变量来接受递归处理的结果
        res = traverse(head.next)
        
        #后序遍历操作
        condition = forward.val == head.val
        # 在值判别之后，才移动正序指针，递归会隐式的倒序便利
        forward = forward.next 
        
        # 将递归结果联系起来，因为只要有一次递归比较值时，不正确就意味着不是回文链表
        return res and condition 
    
    return traverse(head)

print(isPallindrome(head))

# 优化方法 降低空间复杂度 为 O(1)
# 使用 快慢指针找到中心 以及 反转链表技巧

#首先实现反转链表的算法
# 基于迭代的思想，进行反转链表
# 画图来感受 算法之美！！！
def reverse(head):
    """
    反转链表的顺序，返回 反转之后的头指针
    """
    prev = None
    cur = head
    while cur is not None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    
    return prev

# 优化方法二的主函数
def isPallindrome2(head):
    slow = fast = head
    # 快慢指针
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    # 记录中点位置，用于最后的链表还原
    p = slow
    
    # 判断链表的奇偶数情况
    if fast is not None: # 奇数
        slow = slow.next # 奇数节点的情况 要 slow再走一步，因为slow原本在中点位置，要确保在中点左右遍历的节点数一致
    
    # 反转 slow 节点之后的那部分
    rev = reverse(slow)
    
    #记录反转链表的头节点，用于后续的链表还原
    q = rev
    #与头节点开始遍历，进行比较
    while rev is not None:
        if  head.val != rev.val:
            return False
        head = head.next
        rev = rev.next
    
    # 最后 要恢复 原链表的顺序，即需要再次反转 q 指针的链表
    p.next = reverse(q)
    return  True

print(isPallindrome2(head))
print('还原后的链表倒序遍历结果是：')
traverse(head)


# In[秀操作之纯递归反转链表]
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

head = A = Node(0)
for i in [1,2,3,4,5,6]:
    A.next = Node(i)
    A = A.next

# 正序打印链表
def print_link(head):
    while head is not None:
        print(head.val)
        head = head.next

# 使用递归来进行反转链表
"""
使用递归思想主要需要明确以下两个点：
    1. 必须明确递归函数的行为：即设计的递归函数解决了怎样的问题
    2. 看递归函数，不要跳进递归，而是要根据刚才的函数定义，完善逻辑
"""
# 递归反转给定头节点的整条链表
def reverse(head):
    """
    函数定义： 给定头节点，返回反转后序列的头节点
    """
    # base case
    if head is None: # 对应链表无节点的情况
        return None
    # 对应的base-case是链表只有一个节点时,
    # 即递归栈的栈顶位置，也就是head链表的末尾节点
    if head.next is None: 
        return head
    
    ref = reverse(head.next)
    
    # 后序遍历操作
    end = head.next # end 代表的是ref链表的最后一个元素
    end.next = head # 将 head 接在 ref指示的链表的最后一个元素之上
    head.next = None # 重新设置末尾节点的 next 为空指针
    
    return ref # 返回倒序链表的头节点

print('链表进行反转：')
print_link(reverse(head))

# 进阶 反转链表的 前 N 个节点
point_k1 = None # 用于保存第k+1个节点的指针
def reverseN(head, k):
    global point_k1
    """
    函数定义：反转 以head为头指针的前k个结点，返回反转链表后的头指针
    """
    # base case
    if k == 1: # 实际上指的就是 head 为第 k 个节点
        point_k1 = head.next # 记录第 k+1 个节点，后序会用
        return head
    
    ref = reverseN(head.next, k-1)
    
    # 实质上是纠正上一层递归的 head.next = point_k1 的结果
    # 即当层的 head.next.next 实际为上一层的 head.next
    head.next.next = head
    # 让反转之后的 head 节点和后面的节点连接起来
    head.next = point_k1
    
    return ref

head = A = Node(0)
for i in [1,2,3,4,5,6]:
    A.next = Node(i)
    A = A.next

print('反转链表的前k个节点：')
print_link(reverseN(head, 4))

# 反转链表的一部分
def reverseBetween(head, m, n):
    """
    函数定义： 仅仅只反转链表中给出索引区间为 [m, n]的部分，（索引从 1 开始）
    PS ： 都是闭区间
    """
    # base - case
    # 注意：m 一定是大于等于 n 的
    if m==1: # 如果对应的是前n个节点进行反转
        return  reverseN(head, n)
    
    # 对于 head.next 来说，区间变换为 [m-1, n-1]
    ref = reverseBetween(head.next, m-1, n-1)
    # 将链表头部  与 反转过后的子链表进行拼接
    head.next = ref
    return head


head = A = Node(0)
for i in [1,2,3,4,5,6]:
    A.next = Node(i)
    A = A.next
    
print_link(reverseBetween(head, 2, 3))

# In[秀操作之k个一组反转链表]
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

# 子问题是 反转分组中的k个元素
# 由于 后面的处理方便，这里假设 分组区间是左闭右开的
def reverse(left, right):
    prev = None
    cur = left

    while cur.val != right.val:
        next = cur.next
        cur.next = prev
        prev =cur
        cur = next
        
    # 返回反转后的头节点
    return prev


def reverseKGroup(head, k):
    """
    函数定义：将head指向的链表以k个分组，每个分组自进行反转，若最后不足k个元素
            则不进行反转，最后对所有的分组进行拼接
    """
    # base-case
    temp = head
    for i in range(k):
        if temp is None:  # 对于不满足k个元素的情况
            return head
        temp = temp.next
    
    #正常退出循环的时候，temp指向的是下一个分组的首节点

    # 前序遍历操作：反转 前 k 个元素
    # 由于temp的特殊性质，所以在反转链表的时候采用的是 左闭右开 的区间
    newhead = reverse(head, temp)
   
    # 第二步 ：递归反转后续链表 【由于反转是在递归之前调用的，所以反转是前序遍历操作】
    res = reverseKGroup(temp, k)
   
    # 后秀遍历操作： 将得到的分组连接起来
    head.next = res
    
    return newhead


head = A = Node(0)
for i in [1,2,3,4,5,6]:
    A.next = Node(i)
    A = A.next

print('4分组反转链表：')
print_link(reverseKGroup(head, 4))
