#include <vector>
#include <unordered_map>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

int maxPoints(vector<vector<int>>& points) {
    int n = points.size();
    if (n == 1) {
        return 1;
    }
    int result = 2;
    for (int i = 0; i < n; i++) {
        unordered_map<double, int> cnt;
        for (int j = 0; j < n; j++) {
            if (j != i) {
                cnt[atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])]++;
            }
        }
        for (auto [h, count] : cnt) {
            result = max(result, count + 1);
        }
    }
    return result;
}

int main() {
    vector<vector<int>> points = { {1,1}, {2,2}, {3,3} };
    cout << maxPoints(points) << endl;
    return 0;
}