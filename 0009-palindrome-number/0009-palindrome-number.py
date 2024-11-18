class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_s =str(x) 
        if  x_s == x_s[::-1]:
            return True
             
        else:
            return False    
