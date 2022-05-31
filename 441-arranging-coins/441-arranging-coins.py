class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 2:
            return 1 
        s = 0 
        ctr = 0
        while(s<n):
            ctr=ctr+1
            s = s+ctr
        #print(s,n,ctr)
        if s > n:
            return ctr-1
        return ctr
        