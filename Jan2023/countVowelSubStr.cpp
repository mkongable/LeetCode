#include <vector>
#include <queue>
#include <iostream>
#include <unordered_map>
#include <cmath>
#include <unordered_set>

using namespace std;
    
int countVowelSubstrings(string word) {
    //brute force, check every substring
    unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
    int count = 0;
    for (int i = 0; i < word.size(); i++) {
        unordered_set<char> seen;
        for (int j = i; j < word.size(); j++) {
            if (vowels.find(word[j]) != vowels.end()) { //new vowel
                seen.insert(word[j]);
            } else {
                break;
            }
            if (seen.size() == 5) {
                count++;
            }
        }
    }
    return count;
}