class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visitSet = set()

        def perim(i,j):
            if i>=row or j>=col or i<0 or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in visitSet:
                return 0
            
            visitSet.add((i,j))
            perimeter = perim(i-1,j)+perim(i+1,j)+perim(i,j-1)+perim(i,j+1)
            return perimeter

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    return perim(i,j)
        return 0