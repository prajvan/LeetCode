class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def helper(nums,target,lo,hi):
            
            mid = (hi+lo) // 2
            #print(lo,mid,hi)
            
            if nums[mid] == target:
                return mid
            if lo == mid:
                if target > nums[hi]:
                    return hi+1
                elif target < nums[lo]:
                    return lo
                return lo+1
            elif nums[mid] > target:
                return helper(nums,target,lo,mid)
            else:
                return helper(nums,target,mid,hi)
            
        return helper(nums,target,0,len(nums)-1)