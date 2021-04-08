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
            for j in range(i, h, -h): #注意 索引范围
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
