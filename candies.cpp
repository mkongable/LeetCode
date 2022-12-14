#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <functional>
#include <cmath>
#include <string>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <array>
#include <bitset>



using namespace std;

int minimumCost(vector<int>& cost) {
    // sort the cost vector
    // start at the end and add the cost of the last two elements
    // skip the next element
    // repeat until you reach the beginning of the vector
    // return the sum
    sort(cost.begin(), cost.end());
    int sum = 0;
    for(int i = cost.size() - 1; i >= 0; i -= 3){
        sum += cost[i];
        if(i > 0){
            sum += cost[i - 1];
        }
    }
    return sum;
}