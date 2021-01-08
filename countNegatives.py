import itertools
def countNegatives(lt):
    row_len = len(grid[0])
    col_len = len(grid)

    i = 0
    j = row_len - 1
    total = 0

    while i < col_len and j >= 0:
        if grid[i][j] < 0:
            total += col_len - i
            j -= 1
        else:
            i += 1
    return total


grid = [[4,3,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))