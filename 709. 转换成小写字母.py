class Solution(object):
    # 大小写互换： ^= 32
    # 全部变小写： |= 32
    # 全部变大写： &= -33
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        
        return  ''.join([chr(ord(i)|32) for i in str])