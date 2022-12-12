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

int hammingDistance(int x, int y) {
    //convert both numbers to binary of equal length
    string xBin = bitset<32>(x).to_string();
    string yBin = bitset<32>(y).to_string();

    //count the number of differing bits
    int count = 0;
    for(int i = 0; i < xBin.length(); i++){
        if(xBin[i] != yBin[i]){
            count++;
        }
    }
    return count;
}