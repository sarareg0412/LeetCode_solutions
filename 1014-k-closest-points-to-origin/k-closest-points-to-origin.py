class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_closest = []

        def dist(el):
            return math.sqrt(el[0] * el[0] + el[1] * el[1])

        points.sort(key = lambda el: dist(el))
        return points[:k]



