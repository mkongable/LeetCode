#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    //sort by end point
    //initialize the last arrow position to be the first balloon's end point
    //for every balloon in points
        //if balloon's start point is less than the last arrow position, then pop the balloon
        //else, place an arrow at the balloon's end point
    //return the number of arrows

    //sort by end point
    sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });

    int lastArrowPosition = points[0][1];
    int arrows = 1;
    for (int i = 1; i < points.size(); i++) {
        if (points[i][0] <= lastArrowPosition) {
            continue;
        } else { //the start point is greater than the last arrow position
            lastArrowPosition = points[i][1];
            arrows++;
        }
    }

    return arrows;
}

int main() {
    return 0;
}