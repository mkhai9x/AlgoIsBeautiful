'''
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: you can only move either down or right at any point in time.
'''


def minPathSum(grid):
    rows = len(grid)
    cols = len(grid[0])
    if rows == 0 or cols == 0:
        return -1
    # Calculate shortest distances from grid[0][0] to all elements on the first row
    for i in range(1, cols):
        grid[0][i] = grid[0][i] + grid[0][i-1]
    # Calculate the shortest distancecs from grid[0][0] to all elements on the first column
    for i in range(1, rows):
        grid[i][0] = grid[i][0] + grid[i-1][0]

    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[rows-1][cols-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(minPathSum(grid))
