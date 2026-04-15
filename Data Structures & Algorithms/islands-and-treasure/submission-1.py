class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # so what I did was that I started traversing from the gate instead of traversing 
        # at each grid better start to traverse from all gate at once and make a visit set
        # to check if that grid is covered or not and 
        # no need to check the min value as we traversing all the gate at once 
        # so whichever grid is closed will be covered first by default
        
        ROWS, COLS = len(grid) , len(grid[0])
        visit = set()
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))
        def addRoom(r,c):
            if (r<0 or r==ROWS or  c<0 or c==COLS or (r,c) in visit or grid[r][c]==-1):
                return 
            visit.add((r,c))
            q.append([r,c])


        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
                grid[r][c] = dist
            dist+=1
        