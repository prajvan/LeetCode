class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num<=9:
            return True
        if num%10 == 0:
            return False
        return True