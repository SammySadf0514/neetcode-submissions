class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = []
        for point in points:
            newDist = math.sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)
            dist.append([newDist, point])

        dist.sort()
        res = []
        for i in range(k):
            res.append(dist[i][1])

        return res