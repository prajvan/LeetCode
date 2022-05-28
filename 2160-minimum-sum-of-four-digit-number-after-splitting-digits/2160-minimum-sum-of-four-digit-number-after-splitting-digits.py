class Solution:
    def minimumSum(self, num: int) -> int:
        min_sum = 0
        nums = []
        while(num >= 1 ):
            nums.append(num%10)
            num = num//10
        arr_new = sorted(nums)
        return arr_new[0]*10+arr_new[1]*10+arr_new[2]+arr_new[3]
            
        