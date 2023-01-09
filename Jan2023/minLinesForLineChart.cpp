#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

int minimumLines(vector<vector<int>>& stockPrices) {
    //sort stock prices by time
    sort(stockPrices.begin(), stockPrices.end(), [](vector<int>& a, vector<int>& b) {
        return a[0] < b[0];
    });

    if (stockPrices.size() == 1) {
        return 0; //no lines needed for a single point
    }

    //the first two points already make a line
    int lines = 1;
    long double slope = (long double)(stockPrices[1][1] - stockPrices[0][1]) / (stockPrices[1][0] - stockPrices[0][0]);
    for (int i = 2; i < stockPrices.size(); i++) {
        //if the slope remains the same, there is no line needed.
        //if the slope changes, a new line is needed
        long double newSlope = (long double)(stockPrices[i][1] - stockPrices[i - 1][1]) / (stockPrices[i][0] - stockPrices[i - 1][0]);
        if (newSlope != slope) {
            lines++;
            slope = newSlope;
        }
    }
    return lines;
}

int main() {
    vector<vector<int>> stockPrices = {{200,1},{201,499999999},{202,999999998},{203,1000000000}};
    cout << minimumLines(stockPrices) << endl;
    return 0;
}