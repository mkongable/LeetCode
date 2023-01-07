#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    //construct an array of size n+1 where arr[i] = the amount of gas left when you reach the ith gas station when starting from station 0. arr[n] would be the amount of gas left when you reach the station 0 again.
    //arr[0] = 0 by default since you are already there
    //find the minimum of arr and pick that index as the starting point, since you know you are only going higher from there. It is like shifting a graph upwards

    vector<int> arr(gas.size() + 1, 0);
    arr[0] = 0;
    for (int i = 1; i < arr.size(); i++) {
        arr[i] = arr[i-1] + gas[i-1] - cost[i-1];
    }

    //find the min of arr
    int min = arr[0];
    int minIndex = 0;
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] < min) {
            min = arr[i];
            minIndex = i;
        }
    }

    //check the last element of arr to see if it is negative. For reasoning, draw a discrete time graph where the x axis is the index and the y axis is the amount of gas when reaching that index starting from station 0
    if (arr[arr.size()-1] < 0) {
        return -1;
    } else {
        return minIndex;
    }
}

int main() {
    vector<int> gas = {1,2,3,4,5};
    vector<int> cost = {3,4,5,1,2};
    cout << canCompleteCircuit(gas, cost);
    return 0;
}