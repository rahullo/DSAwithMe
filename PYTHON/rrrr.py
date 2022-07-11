# def maxArea(grid):
#   def dfs(i: int, j: int) -> int:
#       if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
#         return 0
#       if grid[i][j] != 1:
#         return 0
#       grid[i][j] = 2
#       return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

#   return max(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))


def maxAreas(grid):
  def dfs(i, j):
    if i<0 or i ==len(grid) or j<0 or j ==len(grid[0]):
      return  0
    if grid[i][j] != 1:
      return 0

    grid[i][j] = 2
    return 1 + dfs(i, j+1)+ dfs(i, j-1) + dfs(i+1, j) + dfs(i-1, j)
  return max(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))
    


print(maxAreas([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(maxAreas([[0,0,0,0,0,0,0,0]]))