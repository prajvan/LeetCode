class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n==1:
            return 0
        if n==2:
            return 1
        matches = 0
        while (n > 2):
            if n%2 == 0:
                matches = matches+n//2
                n = n//2 
            else:
                matches = matches+((n-1)//2)
                n = 1+((n-1)//2)
        if n==2:
            return matches+1
        return matches
        
            
            
        