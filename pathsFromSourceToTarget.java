//https://leetcode.com/problems/all-paths-from-source-to-target/

public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
    //need to perform a backtracking algorithm. Explore a path, and if it doesn't work, backtrack (rewind) and try the next path.
    //Since the graph is a DAG, we don't worry about cycles. If we blindly explore, we either reach the target or a dead end.
    List<List<Integer>> paths = new ArrayList<>();
    List<Integer> path = new ArrayList<>();
    explore(graph, 0, path, paths);
    return paths;
}

public void explore(int[][] graph, int node, List<Integer> path, List<List<Integer>> paths) {
    //add the current node to the path
    path.add(node);
    //if we've reached the target, add the path to the list of paths
    if (node == graph.length - 1) {
        paths.add(new ArrayList<>(path));
    }
    //otherwise, explore each of the neighbors
    else {
        for (int neighbor : graph[node]) {
            explore(graph, neighbor, path, paths);
        }
    }
    //remove the current node from the path
    path.remove(path.size() - 1);
}