class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits)-1
        carry = 1
        while(j >=0 ):
            if digits[j]+carry >= 10:
                carry = 1
                digits[j] = digits[j]+carry-10
                j = j-1
            else:
                digits[j] = digits[j]+carry
                carry = 0
                j=j-1
        if carry ==0:
            return digits
        return [1]+digits
        