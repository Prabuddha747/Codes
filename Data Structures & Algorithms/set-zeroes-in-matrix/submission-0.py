class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        extrarow = [0]*row
        extracol = [0]*col
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    extrarow[i]=1
                    extracol[j]=1
        
        for i in range(row):
            for j in range(col):
                if extrarow[i]==1 or extracol[j]==1:
                    matrix[i][j]=0
        
        