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

bool isHappy(int n) {
  // use a set to keep track of the numbers we've seen
    set<int> seen;
    while (n != 1) {
        // if we've seen this number before, return false
        if (seen.find(n) != seen.end()) {
            return false;
        }
        // add the number to the set
        seen.insert(n);
        // calculate the sum of the squares of the digits
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        // set n to the sum
        n = sum;
    }
    return true;  
}