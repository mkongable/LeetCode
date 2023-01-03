#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

bool wordPattern(string pattern, string s) {
    map<char, string> m;
    set<string> st;
    vector<string> v;
    int i = 0, j = 0;
    while (i < s.size()) {
        if (s[i] == ' ') {
            v.push_back(s.substr(j, i - j));
            j = i + 1;
        }
        i++;
    }
    v.push_back(s.substr(j, i - j));
    if (v.size() != pattern.size()) return false;
    for (int i = 0; i < pattern.size(); i++) {
        if (m.find(pattern[i]) == m.end()) {
            if (st.find(v[i]) != st.end()) return false;
            m[pattern[i]] = v[i];
            st.insert(v[i]);
        } else {
            if (m[pattern[i]] != v[i]) return false;
        }
    }
    return true;
}

int main() {
    string pattern = "abba";
    string s = "dog cat cat dog";
    cout << std::boolalpha << wordPattern(pattern, s) << endl;
    return 0;
}