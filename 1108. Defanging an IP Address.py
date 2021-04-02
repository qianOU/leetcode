# 字符串替换函数，底层使用的 StringBuffer 比较耗时

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return ''.join(i if i.isdigit() else '[.]' for i in  address)
        