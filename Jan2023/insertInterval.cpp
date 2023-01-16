#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    //find index of interval that intersects with start point of newInterval
    //find index of interval that intersects with end point of newInterval
    //merge the two intervals into a bigger interval
    //add the invervals to a result vector, ensuring that no smaller overlapping intervals are added

    //find index of interval that intersects with start point of newInterval
    int startIndex = -1;
    int endIndex = -1;

    for (int i = 0; i < intervals.size(); i++) {
        if (intervals[i][0] <= newInterval[0] && intervals[i][1] >= newInterval[0]) {
            startIndex = i;
        }
        if (intervals[i][0] <= newInterval[1] && intervals[i][1] >= newInterval[1]) {
            endIndex = i;
        }
    }

    //merge the two intervals into a bigger interval
    vector<int> mergedInterval;
    if (startIndex == -1 && endIndex == -1) {
        //no overlap detected, free insert
        mergedInterval = newInterval;
    } else if (startIndex == -1 && endIndex != -1) {
        //merge end index interval with the new interval
        mergedInterval = {newInterval[0], intervals[endIndex][1]};
    } else if (startIndex != -1 && endIndex == -1) {
        //merge start index interval with the new interval
        mergedInterval = {intervals[startIndex][0], newInterval[1]};
    } else {
        //merge start index interval with end index interval
        mergedInterval = {intervals[startIndex][0], intervals[endIndex][1]};
    }

    //create result vector
    vector<vector<int>> result;

    //add all intervals except those overlapping with the merged interval
    for (int i = 0; i < intervals.size(); i++) {
        if (mergedInterval[0] <= intervals[i][0] && intervals[i][0] <= mergedInterval[1] || mergedInterval[0] <= intervals[i][1] && intervals[i][1] <= mergedInterval[1]) {
            //intersection, do nothing
        } else {
            result.push_back(intervals[i]);
        }
    }

    //add the merged interval
    result.push_back(mergedInterval);

    //move the merged interval to the correct position
    for (int i = result.size() - 1; i > 0; i--) {
        if (result[i][0] < result[i - 1][0]) {
            vector<int> temp = result[i];
            result[i] = result[i - 1];
            result[i - 1] = temp;
        } else {
            break;
        }
    }
    return result;
}

int main() {
    vector<vector<int>> intervals = {{1,3},{6,9}};
    vector<int> newInterval = {2,5};
    vector<vector<int>> result = insert(intervals, newInterval);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i][0] << " " << result[i][1] << endl;
    }
    return 0;
}