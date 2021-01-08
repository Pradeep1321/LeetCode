def busyStudent(startTime, endTime, queryTime):
    pair = zip(startTime,endTime)
    count = 0
    result = [1 for i in pair if (i[0] <= queryTime <= i[1])]
    return sum(result)

startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5

print(busyStudent(startTime, endTime, queryTime))
