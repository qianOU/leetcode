class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        total1, total2 = sum(array1), sum(array2)
        if (total1 + total2) % 2:
            return []
        target = (total1 + total2) / 2
        
        n1, n2 = len(array1), len(array2)
        
        flag = 0
        # 确定 array1 比较长
        if n1 < n2:
            array1, array2 = array2, array1
            n1, n2 = n2, n1
            total1, total2 = total2, total1
            flag = 1 # 控制是否进行了交换的标志
 

        array1 = set(array1)
        # 每次遍历比较短的序列
        for i in array2:
            j =  -total2 + i + target
            if j in array1:
                return [int(j), i] if not flag else [i, int(j)]
                break
        
        return []