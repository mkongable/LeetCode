#include <iostream>
#include <string>

using namespace std;

int findLUSlength(string a, string b) {
    //if a and b are not equal, then the longest uncommon subsequence is the longer string
    if (a != b) return a.size() > b.size() ? a.size() : b.size();
    //if a and b are equal, then the longest uncommon subsequence is -1
    return -1;
}