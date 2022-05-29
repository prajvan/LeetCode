class Solution:
    def caluculateSum(self,arr,odd_len):
        rsum = 0
        if odd_len==1 or odd_len==len(arr):
            return sum(arr)
        start_idx = 0
        n = len(arr)
        while(start_idx <= n-odd_len):
            end_idx = start_idx+odd_len
            rsum = rsum+sum(arr[start_idx:end_idx])
            start_idx = start_idx+1
        print(rsum)
        return rsum
    
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        if n==0:
            return 0
        if n == 1:
            return arr[0]
        if n==2:
            return arr[0]+arr[1]
        
        rval = 0
        odd_len = 1
        while(odd_len <= n):
            rval = rval + self.caluculateSum(arr,odd_len)
            #print(rval)
            #print(odd_len)
            odd_len = odd_len+2
        return rval
        