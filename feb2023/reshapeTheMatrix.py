# https://leetcode.com/problems/reshape-the-matrix/
def matrixReshape(self, mat, r, c):
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    # check if the rows*columns is equal to the new rows*columns
    # if not, return the original matrix
    # else, loop thru the matrix inputing it into a new matrix
    if len(mat) * len(mat[0]) != r * c: # invalid case
        return mat
    else:
        # create matrix in r and c dimensions
        matrix = [[0 for i in range(c)] for j in range(r)]
        row = 0
        column = 0
        for i in range(r):
            for j in range(c):
                matrix[i][j] = mat[row][column]
                column+=1
                if column == len(mat[0]):
                    column = 0
                    row+=1
                
        return matrix
    
mat = [[1,2],[3,4]]
print(matrixReshape(any, mat, 1, 4))