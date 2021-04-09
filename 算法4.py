import random
nums = list(range(1000))
random.shuffle(nums)

# 选择排序
# 时间复杂度 为 O(n**2) 
# 确保当前索引 i 的左侧都是 有序的最小值
def selection(nums):
    n = len(nums)
    for i in range(n-1):
        minx = i
        for j in range(i+1, n):
            if nums[j] < nums[minx]:
                minx = j
        nums[i], nums[minx] = nums[minx], nums[i]
    return nums

# 插入排序 升序排列
# 时间复杂度取决于 输入序列， 大致比选择排序快一倍左右
# 遍历索引 i 的左半部分，在合适位置插入 索引 i 的值
def insert(nums):
    n = len(nums)
    for i in range(1, n): # 需要进行插入排序的索引
        for j in range(i, 0, -1): # 对于每个索引 i 需要插入到左部分,由于要确保左半部分有序，所以使用冒泡方法，两两交换到合适位置
            if nums[j] > nums[j-1]:
                 break
            elif nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums

print(selection(nums) == insert(nums))
        


# shell 排序
# 希尔排序基于 插入排序，但是每次只对小部分数组元素
# 小部分数组元素的间隔是固定的 称为递增子序列
# 这样在最后一部使用插入排序时，已经确保数组中大部分都是局部有序的
# 时间复杂度大多为 O(N**(4/3))
def shell_sort(nunms):
    n = len(nums)
    k = [ ]  # 存放递增子序列
    for _ in range(1, n):
        temp = (3**_ - 1)//2
        if temp > n/3:
            break
        k.append(temp)

    for h in k[::-1]: # 从大的间隔开始遍历
        # 对待每一个间隔 为 h 的子序列进行排序
        for i in range(h, n):
            for j in range(i, h+1, -h): #注意 索引范围
                if nums[j] >= nums[j-h]: break
                elif nums[j] < nums[j-h]:
                    nums[j], nums[j-h] = nums[j-h], nums[j]
    
    return nums

print(shell_sort(nums)==insert(nums))


    
# 自顶向下的 归并排序
# 时间复杂度 为 O(NlogN)
def merge(num1, num2): #合并两个有序数组
    i = j = 0
    n1, n2 = len(num1), len(num2)
    ans = []
    while i < n1 and j < n2:
        if num1[i] < num2[j]:
            ans.append(num1[i])
            i += 1
        else:
            ans.append(num2[j])
            j += 1
    
    if i < n1:
        ans.extend(num1[i:])
    elif j < n2:
        ans.extend(num2[j:])
    
    return ans

# 递归实现归并排序
def merge_sort(nums):
    if len(nums) == 1:
        return nums


    mid = len(nums)//2
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))

print(merge_sort(nums) == shell_sort(nums) == selection(nums))

# 自底向上的归并排序
def mergeBU(nums):
    n = len(nums)
    for k in range(1, n//2+2): # 子数组大小。 n//2+1 无论数组长度是奇数或偶数，都可以确保分成两份
        start = 0 #控制每一轮合并的起始
        while start < n:
            end = min(start + 2*k ,n) # 控制最右边的一个子数组不要越界
            nums[start:end] = merge(nums[start:start+k], nums[start+k:end])
            start = end
    return nums

print(mergeBU(nums) == merge_sort(nums))

# 快速排序 
# 时间复杂度为 O(NlogN), 由于不需要频繁移动数组，所以快排序比归并效率要高
def fast_sort(nums):
    # step1 打乱原数组，随机性方法，避免极端情况的发生
    import random
    random.shuffle(nums)
    

    def sort(nums, start, end):

        # 快排的组操作在递归之前完成
        if start > end:
            return 

        # 选择一个初始划分点
        v = nums[start]
        lo = start + 1 
        hi =  end
        
        while lo<=hi:
            # 尽管在相等的时候进行交换会造成一部分性能损失，但是在某些应用中可以有效避免时间复杂度上升为 O(n**2)
            # 左指针扫描到 nums[lo] >= v的位置停止
            while nums[lo] < v:
                if lo == end: break
                lo = lo + 1

            # 右指针扫描到 nums[hi] <= v 的位置停止  
            while nums[hi] > v:
                if hi == start: break
                hi -= 1
                
            if lo >= hi:
                # lo == hi 的情况当且仅当 nums[start+1...end] 都是小于等于 v 时，会有这种情况
                # 这时应该退出主循环，并且交换 start 和 hi 的元素
                break

            # 进行交换位置
            nums[lo], nums[hi] = nums[hi], nums[lo]
    
            
        # 交换 start 与 hi 最后形成 nums[start, hi-1] <= v <= nums[hi+1, end]
        nums[start], nums[hi] = nums[hi], nums[start]

        # 对无序的两个子部分进行再次交换
        sort(nums, start, hi-1)
        sort(nums, hi+1, end)

    sort(nums, 0, len(nums)-1)
    return nums

print(fast_sort(nums)==merge_sort(nums))


# 三切分快速排序
# 主要应用在重复元素较多的数组排序中，可以将时间复杂度下降为 O(n)
def three_part_sort(nums):
    # step1 打乱原数组，随机性方法，避免极端情况的发生
    import random
    random.shuffle(nums)
    

    def sort(nums, start, end):

        # 快排的组操作在递归之前完成
        if start > end:
            return 

        # 选择一个初始划分点
        v = nums[start]
        # 维护三个指针信息
        # 1. 使得 nums[start...lo-1] 都是小于 v 的
        # 2. nums[lo...i-1] 都是等于 v 的
        # 3. nums[i...hi] 是未定的部分，也是循环需要减少的部分
        # 4. nums[hi+1...end] 都是大于 v 的
        i = start + 1 
        lo = start
        hi =  end
        # 从左到右遍历数组一次
        while i <= hi:
            if nums[i] < v:
                nums[i], nums[lo] = nums[lo], nums[i]
                i += 1
                lo += 1
            elif nums[i] > v:
                nums[i], nums[hi] = nums[hi], nums[i]
                # i += 1
                hi -= 1
            else:
                i += 1
        
        # 需要重新整理的是 < v 和 > v 的子部分
        sort(nums, start, lo-1)
        sort(nums, hi+1, end)
    
    sort(nums, 0, len(nums)-1)

    return nums

print(three_part_sort(nums) == fast_sort(nums))
a = list(range(30))*10
# print(three_part_sort(a))

# 优先队列

# 系统自带接口, 数字越小,优先级越高
from queue import PriorityQueue
# 
a = PriorityQueue(10)
a.put((10,2))
a.put((5,21))
a.put((22,21))

print(a.get(), a.get(), a.get(), a.empty())


# 基于 二叉堆数组结构的 优先级队列
# 值越小优先级越高
# put 和 get 的时间复杂度都素 lgN
# 可以用在 top N 问题中

class myPriorityQueue:
    def __init__(self, max):
        self.nums = [None]*(max+1)
        self.n = 0
    
    # 下沉有序
    def sink(self, k):
        while 2*k <= self.n:
            tmp = 2*k # 记录直接子节点的最小值
            if tmp < self.n and self.nums[2*k] > self.nums[2*k+1]: tmp = 2*k+1
            if self.nums[k] <= self.nums[tmp]:
                break
            else:
                self.nums[k], self.nums[tmp] = self.nums[tmp], self.nums[k]

            k = tmp

    # 上浮有序
    def swim(self, k):
        while k > 1:
            parent = k//2
            if self.nums[k] < self.nums[parent]:
                self.nums[k], self.nums[parent] = self.nums[parent], self.nums[k]
            else:
                break

            k //= 2
    
    def empty(self):
        return self.n == 0

    def size(self):
        return self.n
    
    def put(self, k):
        self.n += 1
        try:
            self.nums[self.n] = k # 将新元素插入数组最后一部分
        except IndexError:
            self.nums.append(k)
        finally:
            self.swim(self.n) # 将新插入的元素上浮到相应的位置
    
    def get(self):
        cur = self.nums[1]
        self.nums[1], self.nums[self.n] = self.nums[self.n], self.nums[1] #交换 1 和 N 的位置
        self.nums[self.n] = None # 将要被弹出的元素置为 空
        self.n -= 1 # 弹出元素,队列长度减一
        self.sink(1) # 下沉交换到1位置的元素
        return cur


import random   
test = myPriorityQueue(10)
for i in [random.randint(1,100) for i in range(20)]:
    test.put(i)
for i in range(18):
    print(test.get())


# 堆排序
def heap_sort(nums):
    n = len(nums)
    # 下沉有序 小值优先级越高,排越前面
    def sink( k):
        while 2*k <= n:
            tmp = 2*k # 记录直接子节点的最小值
            if tmp < n and nums[2*k] < nums[2*k+1]: tmp = 2*k+1 # tmp<k 控制了索引不越界
            if nums[k] >= nums[tmp]:
                break
            else:
                nums[k], nums[tmp] = nums[tmp], nums[k]

            k = tmp #转到子节点,进行判断是否需要再下沉
    

    # step1 构建二叉堆数组
    nums = [0, *nums] 
    # 倒序从中点处,进行下沉有序操作 
    for k in range(n//2, 0, -1):
        sink(k)
    # 堆排序操作
    while n > 1:
        nums[1], nums[n] = nums[n], nums[1] # 交换堆顶和堆底元素
        # 对堆顶元素进行下沉有序操作
        n -= 1
        sink(1)
    return nums[1:]

print(heap_sort([random.randint(0, 100) for i in range(100)]))

