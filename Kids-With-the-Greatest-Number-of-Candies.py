def kidsWithCandies(candies, extraCandies):
    output = []
    for i in candies:
        if i + extraCandies >= max(candies):
            output.append(True)
        else:
            output.append(False)
    return output




candies = [12,1,12]
extraCandies = 10
print(kidsWithCandies1(candies,extraCandies))

