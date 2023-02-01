#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> numberOfLines(vector<int>& widths, string s) {
    // move thru the string finding corresponding widths
    // add up th widths until s.charAt(i) + sum > 100
    // if so, increment the line count and reset the sum
    // return the line count and the sum
    int sum = 0;
    int lineCount = 1;
    for (int i = 0; i < s.length(); i++) {
        int charWidth = widths[s[i] - 'a'];
        if (sum + charWidth > 100) {
            lineCount++;
            sum = charWidth;
        } else {
            sum += charWidth;
        }
    }
    return {lineCount, sum};
}