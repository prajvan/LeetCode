class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n<=1:
            return [0]
        if n==2:
            return [-1,1]
        rl = []
        sumi=((n-1)*(n-2))//2
        
        for i in range(n-1):
            rl.append(i)
        rl.append(-1*sumi)
        return rl
                
        