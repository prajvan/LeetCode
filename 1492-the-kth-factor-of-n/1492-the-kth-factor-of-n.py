class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k == 1:
            return 1
        rl = []
        import numpy as np
        for i in range(1,n+1):
            if n%i == 0:
                rl.append(i)
        if k > rl.__len__():
            return -1
        return rl[k-1]
                
        