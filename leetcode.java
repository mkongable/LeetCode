public int minFallingPathSum(int[][] matrix) {
    //create a mirror matrix that will also serve as an OPT table
    //OPT(i, j) = the minimum falling path sum that ends at element i,j
    //OPT(i, j) = min(OPT(i-1, j-1), OPT(i-1, j), OPT(i-1, j+1)) + matrix[i][j]
    //we want the min of the bottom row of OPT
    int[][] OPT = new int[matrix.length][matrix[0].length];
    //copy the first row of matrix into the first row of OPT
    for (int j = 0; j < matrix[0].length; j++) {
        OPT[0][j] = matrix[0][j];
    }
    //fill the rest of the OPT table
    for (int i = 1; i < matrix.length; i++) {
        for (int j = 0; j < matrix[0].length; j++) {
            //if j is the first column, then we can't look at j-1
            if (j == 0) {
                OPT[i][j] = Math.min(OPT[i-1][j], OPT[i-1][j+1]) + matrix[i][j];
            }
            //if j is the last column, then we can't look at j+1
            else if (j == matrix[0].length - 1) {
                OPT[i][j] = Math.min(OPT[i-1][j-1], OPT[i-1][j]) + matrix[i][j];
            }
            //otherwise, look at all three neighbors
            else {
                OPT[i][j] = Math.min(OPT[i-1][j-1], Math.min(OPT[i-1][j], OPT[i-1][j+1])) + matrix[i][j];
            }
        }
    }
    //return the min of the bottom row of OPT
    int min = Integer.MAX_VALUE;
    for (int j = 0; j < matrix[0].length; j++) {
        min = Math.min(min, OPT[matrix.length-1][j]);
    }
    return min;
}