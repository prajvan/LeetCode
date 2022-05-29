class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0
        while(n > 0):
            xor = xor^(start+2*(n-1))
            n = n-1
        return xor
        