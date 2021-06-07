# LeetCode 刷题笔记

## 杂记

1. 有关==循环的判别== 可以使用`快慢指针`来甄别，如果快指针追上了慢指针说明存在循环

2. 有关链表或者二叉树的 逆转输出，可以采用 后序遍历的方式完成。（PS：一般对于递归先用 temp 变量暂存，之后在后序遍历的过程中，使用暂存变量，完成逆转逻辑）

3. 当需要对两条序列进行扫描对比的时候，常用的优化算法是 先扫描==较短==的那一条序列

4. 查找子序列可以使用堆栈的思想

5. 使用 sort 排序之前可以思考是否可以通过一次遍历来获取最大的k个值

6. 要求正序输出 可以使用栈结构：==逆序入栈==,  也就等效于==正序出栈==

7. 如果leetcode报类型错误时，很可能是因为自己在IDLE中取消了对于某种类型的注释造成的

8. “之”，“锯齿形”遍历都是具有先入后出的特性（对于孩子节点而言），使用栈来保存当前遍历的节点的孩子节点，（PS: 每一层的输出可以通过调整奇偶层 左右 节点不同的入栈顺序来保证，如果要求从左到右，则先入栈右子节点， 如果要求是从右到左则先入栈左子节点）

9. 二维矩阵的斜对角线遍历规则
    * 主对角线： $j - i = k$
    * 副对角线： $j + i = k$
    
10. Python的整数除法是向`-∞`取整的

11. `坑`：
    
      1. 对于大数， 如果直接 float 转换成 int 会发生==精度损失==，所以在 类型转换的时候需要特别注意。可以使用decimal 实现高精度的浮点计算。
    
12. 两条直线是否平行，可以使用向量积 $a*b*sin(\theta)==0$判别

13. 计算任何日期是属于星期几：==蔡勒公式==[蔡勒公式_百度百科 (baidu.com)](https://baike.baidu.com/item/蔡勒公式)

     

## 位运算

#### 异或运算

```python
1.交换律(异或可以交换位置)：a ^ b ^ c <=> a ^ c ^ b
2.任何数与0异或为任何数 0 ^ n => n
3.相同的数异或为0: n ^ n => 0
4 4i⊕(4i+1)⊕(4i+2)⊕(4i+3)=0 # 异或的性质 1^2^3 = 0
```

1. 异或运算 可以 用于找出字符串中出现奇数次的那唯一一个单词. 可以用于处理==判别回文序列==

#### 逻辑与 &

1. n & (n-1) 可以用来消除最后一个1（n的二进制表示最后一位1）

#### 大小写转换使用位运算

```shell
1. （--大小写互换--）大写变小写、小写变大写 : 字符 ^= 32;
2. (--全部小写--)大写变小写、小写变小写 : 字符 |= 32;
3. （--全部大写--）小写变大写、大写变大写 : 字符 &= -33;
```

#### 位运算符 运算的 优先级是 低于 数学运算符的

<hr>
#### 有关于 2 的 幂函数，都可以通过位运算进行



## 树

### 特性

1. 我们知道在树（甚至图）中，**所有节点的入度之和等于出度之和**
2. 树的修改需要借助 递归 的方式
3. 要求树的深度最小，一般需要联想到平衡性，【中点性质】

### 二叉搜索树

1. 二叉搜索树的==中序遍历==得到的是==单调递增==的序列

    

### 完全二叉树

1. 根节点在 0 层， 第h层的节点数是 2^h,
2. 排列是紧密靠左的，因此对于最大层数为 h 的完全二叉树，节点个数一定在 [2^h ,2^(h+1) −1] 的范围内，可以在该范围内通过`二分查找`的方式得到完全二叉树的节点个数。
3. 如果 h 层是满节点，那么节点总数是 2^(h+1) - 1
4. ==对于二叉树每一个节点的路径可以抽象为数字的二进制表示==，除了最高位，每一位都可以抽象为节点路径的一次选择，0表示选择左子树，1 表示右子树 ，从==次高位到最低位表示的是树从根节点开始选择的路径==

### 树的序列化与反序列化

1. 如果对 `空节点用特殊符号进行标记`的话，则单靠前序，后序都可以进行反序列化还原树，而==单靠中序遍历不能完成==

2. 如果`没有`对 空节点进行特殊标记，则需要两种遍历方式搭配使用，即 前+中，后+中，但是 前+中 不可以。

3. 如果是二叉搜索树的话，可以使用前 or 后序遍历，再搭配二分查找完成反序列化。或者 二叉树可以通过前序序列或后序序列和中序序列构造（即与2相同）。

4. 还原顺序：
    * 如果是根据后序遍历得到的结果进行反序列化，需要先还原右子树，其次是左子树
    * 如果是根据前序遍历得到的结果进行反序列化，需要先还原左子树，其次是右子树

5. 确保树的==平衡性==

    使用的策略主要是找寻给定序列的中点为root节点，左半部分为左子树，右半部分为右子树 即可。

### 迭代 中序遍历

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        # 隐含栈
        stack = []
        # 把当前节点的完全左子树路径压入栈
        def order(root):
            while root is not None:
                stack.append(root)
                root = root.left
        
        order(root) # 将根节点的完全左子树路径部分压入栈
        ans = []
        while stack:
            top = stack.pop() # 栈顶元素即为 最左端元素 出栈
            ans.append(top.val)
            order(top.right) # 将当前节点的右子树部分也入栈
            
        
        return ans
```



### 迭代 前序遍历

````python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        stack=[root]
        res=[]
        while stack:
            s=stack.pop()
            res.append(s.val)
            # 前序 要求 root left left 所以子节点要求倒序入栈
            if s.right:
                stack.append(s.right)
            if s.left
                stack.append(s.left)
        return res
````

### 迭代 后序遍历

```python
# 由于 前序遍历的顺序 是 root left right
# 而后序遍历的顺序为 left right root,倒转一下就是 root right left
# 恰巧就是 前序遍历中 左右子节点交换位置部分，最后再翻转成原状态即可
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        stack=[root]
        res=[]
        while stack:
            s=stack.pop()
            res.append(s.val)
            if s.left:#与前序遍历相反
                stack.append(s.left)
            if s.right:
                stack.append(s.right)
        return res[::-1] # 翻转回原状态

```



### 找寻最大的第k个元素

使用 生成器来 惰性生产值，这样只需要生成k个即可，节约了时间

### 填充每个节点的下一个右侧节点指针

采用前序遍历的方式，实现dfs逻辑即可

==注意：== 树的题目，使用DFS解法时，一定要注意迭代方式 

### 并查集

1. 并查集实质是用数组来实现树的层次结构
2. 因此==对于连通量的判断，需要借助变量==，每当 union 不同组时， count - 1
3. 直接对于 数组 的去重计数，往往大于等于实际 连通量 的数量，因为 并查集里面的 root 节点是存在 层级关系的，所以每个组的父亲节点 并不一定意味着是 根节点



## 堆与优先队列

1. 优先队列 一个 item 可以 存放 多个元素

```python
from queue import PriorityQueue as pq
q = pq()

q.put((priority, 1, 0, 1)) # priorty 之后的元素是 item成员

优先对列是否为空
需要使用 内置方法 empty 判别
```



## 类型

### 动态规划

1. 判断子序列 s 是否存在于 t 中

     dp\[i\]\[j\] 表示字符串 *t* 中从位置 i 开始往后直到字符 j 第一次出现的位置

    base-case: dp\[len(t)\][*] = m 表示不存在




## DFS

1. python 中 dfs 可以基于`协程`的写法 (十分优雅！！)

     ```python
    class Solution:
        def leafSimilar(self, root1, root2):
            def dfs(node):
                if node:
                    if not node.left and not node.right:
                        yield node.val
                    yield from dfs(node.left)
                    yield from dfs(node.right)
    
            return list(dfs(root1)) == list(dfs(root2))
    ```
    

## string类型题目

### 判断括号的有效性

有效的具有括号的字符串有以下特性：

1. 字符串中有相同数量的 `"("` 和 `")"`。
2. 从左至右遍历字符串，统计当前 `"("` 和 `")"` 的数量，永远不会出现 `")"` 的数量大于 `"("` 的数量

## 栈

1. 计算器运算

    将 符号和数字一起 视为一个整体，如果是 +， - 将数字压入栈，如果是乘除则与栈顶元素运算后入栈，最后对栈求和即可。（初始化时，设定符号为 + ）
    
2. 逆序处理序列，需要想到利用栈来处理

    ### 单调栈

    1. 单调栈可以用来找寻第一个大于/ 小于 某个元素的索引

    2. 单调栈用于求一类 next greater number 问题，时间复杂度为 0(N)

    3. 在接雨水等问题中，需要同时确定左右边界，左边界（小于 nums[i] 的左侧第一个元素索引）， 右边界（小于nuns[i]的右侧第一个元素索引），可以使用两个单调栈来维护处理。

        ```python
        # 右边界的确定
        stack = []
                for i in range(n):
                    more_less[i][0] = nums[i]
                    # 栈顶元素如果大于 nums[i] 也就意味着找到右边界
                    while stack and nums[stack[-1]] > nums[i]:
                        item = stack.pop()
                        more_less[item][-1] = i
                    stack.append(i)
                # 还保留在栈中的元素，就是无右边界，设置为n
                while stack:
                    item = stack.pop()
                    more_less[item][-1] = n
        
           
        # 左边界的确定            
                stack = []
                for i in range(n-1, -1, -1):
                    # 栈顶元素如果大于 nums[i] 也就意味着找到左边界
                    while stack and nums[stack[-1]] > nums[i]:
                        item = stack.pop()
                        more_less[item][1] = i+1 # 因为浅醉和每一个元素都是左闭右开的，所以左边界要+1
        
                    stack.append(i)
                # 还保留在栈中的元素，就是无左边界，设置为0, presum[0] == 0
                while stack:
                    item = stack.pop()
                    more_less[item][1] = 0
        ```

        

    

## 链表

1.  **环形链表**

    其处理的过程包括两步骤：

    * 使用快慢指针（1步，2步间隔）找到相交点

    * 从相交节点 以及 头节点同时出发，遇见的第一个节点就是环的起始点

## 排序

### 归并排序

1. 归并排序的base-case:

    * 分解后只有一个元素的情况，注意如果是链表等还需要将该节点next指针指向 None
* 分解后没有元素的情况

### Top K 问题

1. 使用排序算法之后，在获取前 k 位
2. 使用优先队列（堆排序），确保插入的有序性

### 最大不重复子区间/时间调度/射气球问题

1. 都是利用贪心算法， 并且基于 区间==右边界==进行排序处理

### 数组重排序组合成最小的数

1. 主要是需要知道 a, b 两个数字，在组合时，谁排前面先组合。

    有以下规则：假设 a,b 都是字符串

    ​	a + b < b + a 说明 a 在b 前面， b 在 a 后面结合

### 查看值是否落入某个定长的范围内的时候，使用桶排序

### 基数排序

1. 基数排序是一种不基于比较的排序算法，时间复杂度为 0(n)[基数排序_百度百科 (baidu.com)](https://baike.baidu.com/item/基数排序)

    ```python
    import math
     
    def sort(a, radix=10):
        """a为整数列表， radix为基数"""
        # 这里的 + 1 十分关键
        K = math.ceil(math.log(max(a), radix)) + 1 # 用K位数可表示任意整数, 注意需要加 1，因为是实际中 数字的长度， == len(str(max(a)))
        
        bucket = [[] for i in range(radix)] # 不能用 [[]]*radix
        for i in range(1, K+1): # K次循环
            for val in a: # 个位数 -> 十位数 ->...不断入桶再合并的过程
                bucket[val%(radix**i)//(radix**(i-1))].append(val) # 析取整数第K位数字 （从低到高）
            del a[:]
            for each in bucket:
                a.extend(each) # 桶合并
            bucket = [[] for i in range(radix)]
    ```

    

### 桶排序 / 计数排序

1. 桶排序也是一种不是基于比较的算法，时间复杂度为 0(N)，重点是需要设置合理的桶大小

2. 计数排序，是桶大小为1的时候的特殊桶排序

## 二分查找

### 1. 常见的有基于 索引 的二分查找

### 2. 基于 值 的二分查找也是十分重要的

eg: [378. 有序矩阵中第 K 小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)



## 滑动窗口

1. 在使用滑动窗口技巧的时候，有时没必要保持窗口元素的有序性的时候，可以使用队列即【普通列表】进行存储。

2. 在有些题目里面，保持窗口元素的有序性是十分有必要的，可以使用【有序列表】数据结构，甚至可以搭配二分搜索来使用，降低时间复杂度。[220. 存在重复元素 III](https://leetcode-cn.com/problems/contains-duplicate-iii/)

    ```python
    # 导入 有序列表 数据结构
    from sortedcontainers import SortedList
    
    class Solution:
        def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
            # O(N logk)
            window = SortedList()
            for i in range(len(nums)):
                # len(window) == k
                if i > k: # 窗口滚动
                    window.remove(nums[i - 1 - k])
                window.add(nums[i]) # 保证插入有序
                # 找寻 小于 nums[i] 的最大索引值
                idx = bisect.bisect_left(window, nums[i])
                if idx > 0 and abs(window[idx] - window[idx-1]) <= t:
                    return True
                if idx < len(window) - 1 and abs(window[idx+1] - window[idx]) <= t:
                    return True
            return False
    
    ```

    

3. 

## 并查集

1. 图问题

2. 连通性问题

3. 交换元素问题【1722】

    比如 [1, 2], [0,1]  则意味着 0，1，2可以任意交换位置，其实质也就是同一个连通量



## 图

### 1无向图：.

* ==并查集== 十分重要
* 可以借助==并查集== 来 判断是否有环的存在

### 有向图：

* 邻接表的构建   +  路径记录

* 环路的判断 

*  

    * （`拓扑排序`：借助出/入度）使用BFS时需要借助 ==节点的出度 或者 入度==，将 入度为 0 的 节点作为搜索的第一步入队列，之后要维护节点的 入/ 出 度 的变换， 将入度为 0 的节点作为搜索的第二部入队列

    * 使用 DFS 是要 使用 ==状态记录表 区分 本次 DFS 搜索走过的路径==，用来判断是否有环路，用其它的符号标记不会产生环路的节点，来剪枝。

        

## BFS

1. BFS 中十分重要的一点，就是必修明确入队列的条件。以及去重
    * 在寻求最少花费的时候，一个节点可能会被遍历多次，为了避免一个节点的无线重复遍历，这时候的入队列的条件可以设置为 ==使得从起点到达该点的费用变少的时候，才入队列==

## 整数相关

### 1. 获得某一个整数各个位数上的值

```python
x = 13211234
ans = []
while x:
    ans.append(x%10)
    x /= 10 # 进位
```

### 素数删表法

```python
# 素数删表法
def prime(n):
    for i in range(2, int(n**.5)+1):
        if n % i:
            return False
    return True

def prime_table(n):
    ans = [True]*(n+1)
    for x in range(2, int(n**.5+1)): # 只需要扫描到 sqrt(n) 即可
        if prime(x):
            for j in range(x**2, n, x):  # 优化手段一， 从 x**2 开始，可以避免重复遍历
                ans[x] = False # 素数的倍数，不是素数
    
    # 返回素数的个数
    return sum(ans[2:])
```

## 数组

1. 差分法

    主要处理 : 上车下车，上飞机下飞机等，在区间某一个特定时间里人数最多的一类问题

    例子： [人口最多的年份 - 人口最多的年份 - 力扣（LeetCode） (leetcode-cn.com)](https://leetcode-cn.com/problems/maximum-population-year/solution/ren-kou-zui-duo-de-nian-fen-by-leetcode-5m7r4/)

    ```python
        # 差分数组法
        def maximumPopulation(self, logs: List[List[int]]) -> int:
            delta = [0]*101 # 差分数组
            offset = 1950
            for i, j in logs:
                delta[i-offset] += 1
                delta[j-offset] -= 1 # 死亡年份 - 1
            
            ans = 0
            count = 0
            mx = 0
            for i in range(101):
                count += delta[i] # 在某个时间的人数，是之前还留在系统的人数之和
                if count > mx:
                    mx = count
                    ans = i + offset
    ```

2. 循环数组问题

    1. 要懂得使用==负数索引 以及 (1+i)%n==，两个规律

3. 树状数组

