#include <string>
#include <iostream>

using namespace std;

bool detectCapitalUse(string word) {
    //returns true if all the letters in the word are capitals, or if all the letters are not capitals, or if only the first letter is capital
    int count = 0; //number of capital letters
    for (int i = 0; i < word.size(); i++) {
        if (word[i] >= 'A' && word[i] <= 'Z') count++;
    }
    if (count == word.size() || count == 0) return true;
    if (count == 1 && word[0] >= 'A' && word[0] <= 'Z') return true;
    return false;
}