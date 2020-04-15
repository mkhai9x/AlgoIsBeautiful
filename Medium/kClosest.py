'''
We have a list of points on the plane.  
Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  
The answer is guaranteed to be unique (except for the order that it is in.)
'''


def kClosest(points, K):
    points.sort(key=lambda P: P[0]**2 + P[1]**2)
    return points[:K]


points = [[1, 3], [-2, 2]]
K = 1
assert kClosest(points, K) == [[-2, 2]]
points = [[3, 3], [5, -1], [-2, 4]]
K = 2
assert kClosest(points, K) == [[3, 3], [-2, 4]]
points = [[0, 1], [1, 0]]
K = 2
assert kClosest(points, K) == [[0, 1], [1, 0]]
