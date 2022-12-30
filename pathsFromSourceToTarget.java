//https://leetcode.com/problems/all-paths-from-source-to-target/

public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
    //need to perform a backtracking algorithm. Explore a path, and if it doesn't work, backtrack (rewind) and try the next path.
    //Since the graph is a DAG, we don't worry about cycles. If we blindly explore, we either reach the target or a dead end.
}