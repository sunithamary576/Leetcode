class Solution(object):
    def isPalindrome(self, s):
        c="".join(char.lower() for char in s if char.isalnum())
        return c==c[::-1]
               