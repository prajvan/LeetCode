class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        rlist = []
        for query in queries:
            x,y,r = query
            inside_points = 0
            for point in points:
                x1,y1 = point
                if (x-x1)*(x-x1)+(y-y1)*(y-y1)<= r*r:
                    inside_points+=1
            rlist.append(inside_points)
        return rlist
        