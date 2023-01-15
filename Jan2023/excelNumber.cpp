#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int titleToNumber(string columnTitle) {
    int weight = pow(26, columnTitle.size() - 1);
    int result = 0;
    for (char c : columnTitle) {
        int digit = c - 'A' + 1;
        result += digit * weight;
        weight /= 26;
    }
    return result;
}