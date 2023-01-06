#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int maxIceCream(vector<int>& costs, int coins) {
    //sort the costs
    //start grabbing the cheapest in a greedy fashion
    //if the cost is greater than the coins, then return the number of ice creams
    int iceCreams = 0;
    sort(costs.begin(), costs.end());
    for (int i = 0; i < costs.size(); i++) {
        if (costs[i] <= coins) {
            coins -= costs[i]; //purchase the ice cream
            iceCreams++;
        } else {
            break; //cannot afford, too poor
        }
    }
    return iceCreams;
}