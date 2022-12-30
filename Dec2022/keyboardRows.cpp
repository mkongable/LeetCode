#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <functional>
#include <cmath>
#include <string>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <array>
#include <bitset>



using namespace std;

vector<string> findWords(vector<string>& words) {
    //create a set for each row
    set<char> row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'};
    set<char> row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'};
    set<char> row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'};
    //create a vector to hold the words that can be typed on one row
    vector<string> result;
    //loop thru the words
    for(int i = 0; i < words.size(); i++){
        //convert the word to lowercase
        string word = words[i];
        transform(word.begin(), word.end(), word.begin(), ::tolower);
        //check if the word can be typed on one row
        bool oneRow = true;
        //check if the word can be typed on row 1
        for(int j = 0; j < word.length(); j++){
            if(row1.find(word[j]) == row1.end()){
                oneRow = false;
                break;
            }
        }
        if(oneRow){
            result.push_back(words[i]);
            continue;
        }
        // need to reset indicator after each row check
        oneRow = true;
        //check if the word can be typed on row 2
        for(int j = 0; j < word.length(); j++){
            if(row2.find(word[j]) == row2.end()){
                oneRow = false;
                break;
            }
        }
        if(oneRow){
            result.push_back(words[i]);
            continue;
        }
        // need to reset indicator after each row check
        oneRow = true;
        //check if the word can be typed on row 3
        for(int j = 0; j < word.length(); j++){
            if(row3.find(word[j]) == row3.end()){
                oneRow = false;
                break;
            }
        }
        if(oneRow){
            result.push_back(words[i]);
            continue;
        }
    }
    return result;
}