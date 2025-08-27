class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True

        t = str(abs(x))
        z = t[::-1]
        k = int(z)
        if negative == True:
            k = -k
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  
        if k < INT_MIN or k > INT_MAX:
            return 0    
        return k
        