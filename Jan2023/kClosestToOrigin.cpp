#include <iostream>
#include <vector>
#include <cmath>
#include <queue>

struct Compare {
    bool operator() (vector<int> a, vector<int> b) {
        if (a[2] > b[2]) return true;
        else return false;
    }
};

using namespace std;

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<vector<int>, vector<vector<int>>, Compare> pq;
    for (int i = 0; i < points.size(); i++) {
        int x = points[i][0];
        int y = points[i][1];
        int dist = x * x + y * y;
        pq.push({x, y, dist});
    }
    vector<vector<int>> res;
    for (int i = 0; i < k; i++) {
        res.push_back({pq.top()[0], pq.top()[1]});
        pq.pop();
    }
    return res;
}