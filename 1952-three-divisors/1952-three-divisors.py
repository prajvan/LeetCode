class Solution:
    def isThree(self, n: int) -> bool:
        if n<=3:
            return False
        i,x = 2,n//2
        ct = 0
        while(i <= x):
            if n%i == 0:
                ct += 1
            i += 1
        if (ct+2)==3:
            return True
        return False