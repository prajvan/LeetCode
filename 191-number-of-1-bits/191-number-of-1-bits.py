class Solution:
    def hammingWeight(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        count = 0
        while(n >= 1):
            rem = n % 2 
            if rem==1:
                count+=1
            n = n // 2
        return count
        