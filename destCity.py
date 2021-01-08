def destCity(paths):
    dicpath = dict(paths)
    value = paths[0][1]
    for i in range(len(paths)):
        value = paths[i][1]
        while value in dicpath.keys():
            value= dicpath.get(value)
    return value

paths = [["B","C"],["D","B"],["C","A"]]
print(destCity(paths))