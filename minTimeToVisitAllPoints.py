def minTimeToVisitAllPoints(points):
    sec = 0
    for i in range(len(points)-1):
        sec+=(max(abs(points[i+1][0] - points[i][0]),abs(points[i+1][1] - points[i][1])))
    return sec

points = [[3,2],[-2,2]]
print(minTimeToVisitAllPoints(points))
