#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

string convertToTitle(int columnNumber) {
    //single digit column supports 26, double supports 26^2, triple 26^3
    //algorithm: keep adding 26 to the power of the next exponent until the column number is reached
    //subtract all the powers of 26 from the column number except for the last one
    //resolve the remaining integer based on the max number of digits
    int digits = 1;
    uint64_t sum = 26;
    while (sum < columnNumber) {
        sum += pow(26, digits + 1);
        digits++;
    }

    //current number of digits is finalized
    //subtract the beginning residuals
    for (int i = 1; i < digits; i++) {
        columnNumber -= pow(26, i);
    }

    //start processing each letter of the remainder, e.g. AABC is (26^3) * 1 + (26^2) * 1 + (26^1) * 2 + (26^0) * 3
    //base 26 conversion

    columnNumber -= 1; //for 0 indexing

    int weight = pow(26, digits - 1);
    string result = "";

    for (int i = 0; i < digits; i++) {
        int digit = columnNumber / weight;
        result += (char)('A' + digit);
        columnNumber -= digit * weight;
        weight /= 26;
    }

    return result;
}

int main() {
    cout << convertToTitle(27) << endl;
    return 0;
}