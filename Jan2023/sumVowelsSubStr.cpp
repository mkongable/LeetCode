#include <vector>
#include <queue>
#include <iostream>
#include <unordered_map>
#include <cmath>
#include <unordered_set>

using namespace std;

long long countVowels(string word) {
    long long count = 0;
    unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
    for (int i = 0; i < word.size(); i++) {
        long long vowelCount = 0;
        for (int j = i; j < word.size(); j++) {
            if (vowels.find(word[j]) != vowels.end()) { //new vowel
                vowelCount++;
            }
            count += vowelCount;
        }
    }
    return count;
}

int main() {
    cout << -5 % 3 << endl;
}