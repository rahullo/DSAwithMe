def floodfill(image, sr, sc, newColor):
  startcolor = image[sr][sc]
  seen = set()

  def dfs(i, j):
    if i < 0 or i==len(image) or j < 0 or j == len(image):
      return
    if image[i][j] != startcolor or (i, j) in seen:
      return
     
    image[i] [j] = newColor
    seen.add((i, j))
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

  dfs(sr, sc)
  return image


print(floodfill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
print(floodfill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))