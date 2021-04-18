# LeetCode 刷题笔记

## 杂记

1. 有关==循环的判别== 可以使用`快慢指针`来甄别，如果快指针追上了慢指针说明存在循环
2. 有关链表或者二叉树的 逆转输出，可以采用 后序遍历的方式完成。（PS：一般对于递归先用 temp 变量暂存，之后在后序遍历的过程中，使用暂存变量，完成逆转逻辑）
3. 当需要对两条序列进行扫描对比的时候，常用的优化算法是 先扫描==较短==的那一条序列
4. 查找子序列可以使用堆栈的思想
5. 使用 sort 排序之前可以思考是否可以通过一次遍历来获取最大的k个值
6. 要求正序输出 可以使用栈结构：==逆序入栈==,  也就等效于==正序出栈==
7. 如果leetcode报类型错误时，很可能是因为自己在IDLE中取消了对于某种类型的注释造成的

## 位运算

#### 异或运算

```python
1.交换律(异或可以交换位置)：a ^ b ^ c <=> a ^ c ^ b
2.任何数与0异或为任何数 0 ^ n => n
3.相同的数异或为0: n ^ n => 0
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

### 二叉搜索树

1. 二叉搜索树的==中序遍历==得到的是==单调递增==的序列

    

### 完全二叉树

1. 根节点在 0 层， 第h层的节点数是 2^h,
2. 排列是紧密靠左的，因此对于最大层数为 h 的完全二叉树，节点个数一定在 [2^h ,2^(h+1) −1] 的范围内，可以在该范围内通过`二分查找`的方式得到完全二叉树的节点个数。
3. 如果 h 层是满节点，那么节点总数是 2^(h+1) - 1
4. ==对于二叉树每一个节点的路径可以抽象为数字的二进制表示==，除了最高位，每一位都可以抽象为节点路径的一次选择，0表示选择左子树，1 表示右子树 ，从==次高位到最低位表示的是树从根节点开始选择的路径==

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
    


