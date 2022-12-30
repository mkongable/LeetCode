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

bool hasGroupsSizeX(vector<int>& deck) {
    // try to partition the deck into groups of the same integer and size

    // map integers to their frequency
    unordered_map<int, int> freq;
    for (int i = 0; i < deck.size(); i++) {
        //check if deck[i] is in the map
        if (freq.find(deck[i]) == freq.end()) {
            //if not, add it
            freq[deck[i]] = 1;
        }
        else {
            //if so, increment the frequency
            freq[deck[i]]++;
        }
    }

    // find the greatest common divisor of all the frequencies
    int gcd = 0;
    for (auto it = freq.begin(); it != freq.end(); it++) {
        gcd = __gcd(gcd, it->second);
    }

    // if the gcd is greater than 1, return true
    if (gcd > 1) {
        return true;
    }
    else {
        return false;
    }
}

int main()
{
    vector<int> deck = { 1, 2, 3, 4, 4, 3, 2, 1 };
    cout << hasGroupsSizeX(deck) << endl;
    return 0;
}