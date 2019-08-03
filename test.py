#Waypoint 7:
import math
def calculate_euclidean_distance_between_2_points(p1, p2):
    result = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    return result
def calculate_euclidean_distance_between_points(point):
    ans = 0
    if len(point) == 1:
        raise ValueError
    for i in range(len(point) - 1):
        ans += calculate_euclidean_distance_between_2_points(point[i], point[i+1])
        return ans
point= [(0, 0), (3,4), (-1,-1)]
print(calculate_euclidean_distance_between_points(point))