class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i):
                temp1= matrix[i][j]
                temp2 = matrix[j][i]
                matrix[i][j]= temp2
                matrix[j][i] = temp1
        
        for i in range(len(matrix)):
            matrix[i].reverse()
        