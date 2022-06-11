class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        import numpy as np
        dl = np.zeros(num_people, dtype = int)
        idx = 0
        
        prev = 1
        while(candies > 0):
            # reset index once reached the final index
            if idx > num_people-1:
                idx = 0
            # check if there are candies available
            if prev > candies:
                dl[idx] = dl[idx]+candies
            else:
                dl[idx] = dl[idx]+prev
            idx=idx+1
            candies = candies - prev
            prev = prev+1
        return dl
            
        