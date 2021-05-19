def minPathSum(grid):
    dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(0, len(grid)):
        dp[i][0] = grid[i][0] + dp[i-1][0]
    for i in range(0, len(grid[0])):
        dp[0][i] = grid[0][i] + dp[0][i-1]
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[len(grid)-1][len(grid[0])-1]


grid = [[1,3,1],[1,5,1],[4,2,1]]
minPathSum(grid)
