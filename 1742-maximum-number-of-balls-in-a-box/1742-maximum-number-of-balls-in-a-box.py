class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def box(i):
            rval = 0
            for i in str(i):
                rval = rval+int(i)
            return rval
        
        freq = defaultdict(int)
        for i in range (lowLimit,highLimit+1):
            rem=box(i)
            freq[rem]=freq[rem]+1
        return max(freq.values())