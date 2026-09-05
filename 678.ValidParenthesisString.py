class Solution(object):
    def checkValidString(self, s):
        low = 0
        high = 0
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char is '*'
                low -= 1   # Treat '*' as ')'
                high += 1  # Treat '*' as '('
                
            if high < 0:
                return False  # Too many ')'
            if low < 0:
                low = 0       # Reset lower bound to 0
                
        return low == 0
