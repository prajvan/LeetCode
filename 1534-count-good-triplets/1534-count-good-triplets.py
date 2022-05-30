class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def is_good(i,j,k):
            a1 = abs(arr[i]-arr[j]) <= a
            b1 = abs(arr[j]-arr[k]) <= b
            c1 = abs(arr[i]-arr[k]) <= c
            return all([a1,b1,c1])
        
        size = len(arr)
            
        return sum(1 for i in range(size-2) for j in range(i+1, size-1) for k in range(j+1, size) if is_good(i,j,k))