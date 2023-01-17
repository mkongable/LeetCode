#include <vector>
#include <queue>
#include <iostream>
#include <unordered_map>
#include <cmath>

using namespace std;

int minFlipsMonoIncr(string s) {
    //take every point as the pivot and find the pivot that gives the minimum number of flips
    //keep a running sum of how many 1's are to the left of the pivot and how many 0's are to the right of the pivot
    //the total number of flips is the sum of the number of 1's to the left of the pivot and the number of 0's to the right of the pivot
    //the pivot will mark the right edge of the 0 frontier
    int leftOnes = 0;
    //populate rightZeroes
    int rightZeroes = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '0') {
            rightZeroes++;
        }
    }

    //slide the pivot to the right, checking as you go
    int minFlips = leftOnes + rightZeroes;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '0') {
            rightZeroes--;
        } else {
            leftOnes++;
        }
        minFlips = min(minFlips, leftOnes + rightZeroes);
    }
    return minFlips;
}

int main() {
    string s = "11011";
    int res = minFlipsMonoIncr(s);
    cout << res << endl;
    return 0;
}