class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0,len(nums)-1
        while(i < j):
            if nums[i]==val and nums[j]==val:
                j-=1
            elif nums[i]!=val and nums[j]==val:
                # no swapping req
                i+=1
                j-=1
            elif nums[i]==val and nums[j]!=val:
                #swap i and j values
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
            else:
                #swap next i with  j
                i+=1
        for idx,value in enumerate(nums):
            if value==val:
                return idx
            