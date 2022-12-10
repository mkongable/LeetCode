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

vector<int> countBits(int n) {
    //list of all powers of two less than n
    vector<int> powersOfTwo;
    for(int i = 0; i <= n; i++){
        if(pow(2, i) <= n){
            powersOfTwo.push_back(pow(2, i));
        }
    }
    vector<int> result;
    // 0 has 0 ones
    result.push_back(0);
    // loop thru and determine the number of ones for each number
    for(int i = 1; i <= n; i++){
        int num = i;
        int count = 0;
        for(int j = powersOfTwo.size() - 1; j >= 0; j--){
            if(num >= powersOfTwo[j]){
                num -= powersOfTwo[j];
                count++;
            }
        }
        result.push_back(count);
    }
    return result;
}

int main()
{
    //call countbits
    vector<int> result = countBits(2);
    // print result as a string
    for(int i = 0; i < result.size(); i++){
        cout << result[i] << " ";
    }
    return 0;
}