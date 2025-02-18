# IBM-CyberStart Group-11
# week-2: Minimum Euclidean Distance

# helper function-1: calculates the Euclidean distance between two points
def euclideanDistance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

# helper function-2: finds the minimum distance from the list of distances
def findMinimumDistance(distances):
    minDistance = float('inf')
    for i in range(len(distances)):
        if distances[i] < minDistance:
            minDistance = distances[i]
    return minDistance

# main function: the points are defined and the distances are calculated
def main():
    points = [(1, 0), (4, 4), (8, 6), (2, 8), (6, 1)]
    distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distances.append(euclideanDistance(points[i], points[j]))
    print(findMinimumDistance(distances))

# main function call
if __name__ == "__main__":
    main()