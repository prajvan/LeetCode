class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev,curr = 0,0
        srt = nums[0]
        while curr < len(nums):
            if nums[curr] == srt:
                curr+=1
            else:
                prev = prev+1
                srt = nums[curr]
                nums[prev] = srt
                print(prev,curr)
                curr+=1
        print(nums)
        return prev+1
        