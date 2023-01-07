#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

bool isIsomorphic(string s, string t) {
    if (s.size() != t.size()) {
        return false;
    }

    //string lengths are equal now, try and force a mapping from one string to another

    unordered_map<char, char> sToT;
    unordered_set<char> discoveredChars;
    for (int i = 0; i < s.size(); i++) {
        if (sToT.find(s[i]) == sToT.end()) {
            if (discoveredChars.find(t[i]) != discoveredChars.end()) {
                return false;
            }
            sToT[s[i]] = t[i];
            discoveredChars.insert(t[i]);
        } else {
            if (sToT[s[i]] != t[i]) {
                return false;
            }
        }
    }

    return true;
}

int main() {
    string s = "badc";
    string t = "baba";
    cout << isIsomorphic(s, t) << endl;
}