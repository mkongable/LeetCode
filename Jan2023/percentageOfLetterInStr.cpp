#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int percentageLetter(string s, char letter) {
    int count = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == letter) {
            count++;
        }
    }

    return floor(count * 100 / (double) s.size());
}