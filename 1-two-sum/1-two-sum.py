class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) ==2:
            return [0,1]
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]].append(i)
            else:
                hm[nums[i]] = [i]
        print(hm)
        id1,id2 = 0,0
        for idx,val in enumerate(nums):
            print(idx,val)
            if (target-val) in hm:
                if target-val == val:
                    if len(hm[val]) > 1:
                        id2 = hm[val][1]
                        id1=idx
                        break
                    else:
                        continue
                else:
                    id1=idx
                    id2 = hm[target-val][0]
                    break     
            
        return [id1,id2]