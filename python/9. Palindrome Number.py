class Solution(object):
    def isPalindrome(self, x):

        x = str(x)
        if x[::-1] != x:
            return False
        else:
            return True